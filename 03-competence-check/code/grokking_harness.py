"""
grokking_harness.py -- training harness for the grokking replication
described in the accompanying README. Reuses the standard minimal
grokking-transformer pattern (decoder-only, 2 layers, no positional-
embedding tricks beyond the standard learned choice) rather than
hand-rolling a custom architecture -- a hand-rolled bug could otherwise
masquerade as "no grokking occurred."

This is a replication of a published result, not a novel claim. See the
README for the full setup, budget, and pass/fail criteria.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


def make_dataset(p, device):
    """All (a, b) pairs for modular addition (a + b) mod p, as a single
    enumerable dataset -- p^2 examples, small enough to hold entirely on
    device for p=97 (9409 examples)."""
    a = torch.arange(p, device=device)
    b = torch.arange(p, device=device)
    aa, bb = torch.meshgrid(a, b, indexing="ij")
    aa, bb = aa.flatten(), bb.flatten()
    labels = (aa + bb) % p
    return aa, bb, labels


def split_dataset(aa, bb, labels, frac_train, seed, device):
    n = len(aa)
    g = torch.Generator(device="cpu").manual_seed(seed)
    perm = torch.randperm(n, generator=g).to(device)
    n_train = int(n * frac_train)
    train_idx, test_idx = perm[:n_train], perm[n_train:]
    return (
        (aa[train_idx], bb[train_idx], labels[train_idx]),
        (aa[test_idx], bb[test_idx], labels[test_idx]),
    )


class GrokkingTransformer(nn.Module):
    """Minimal decoder-only transformer for modular arithmetic, matching
    the standard grokking-literature reference pattern (Power et al. 2022 /
    well-known reproductions): input is [a, b, '='] as 3 tokens (vocab =
    p integers + 1 equals-token), predict the token at the '=' position."""

    def __init__(self, p, d_model=128, n_heads=4, n_layers=2, d_mlp=512):
        super().__init__()
        vocab = p + 1  # p residues + 1 "=" token
        self.p = p
        self.tok_embed = nn.Embedding(vocab, d_model)
        self.pos_embed = nn.Embedding(3, d_model)
        layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=n_heads,
            dim_feedforward=d_mlp,
            dropout=0.0,
            activation="relu",
            batch_first=True,
        )
        self.encoder = nn.TransformerEncoder(layer, num_layers=n_layers)
        self.unembed = nn.Linear(d_model, p, bias=False)

    def forward(self, a, b):
        eq_tok = torch.full_like(a, self.p)  # "=" token id = p
        tokens = torch.stack([a, b, eq_tok], dim=1)  # (batch, 3)
        pos = torch.arange(3, device=tokens.device).unsqueeze(0)
        x = self.tok_embed(tokens) + self.pos_embed(pos)
        mask = nn.Transformer.generate_square_subsequent_mask(3).to(tokens.device)
        out = self.encoder(x, mask=mask, is_causal=True)
        logits = self.unembed(out[:, -1, :])  # prediction at "=" position
        return logits


def accuracy(model, aa, bb, labels, batch_size=4096):
    model.eval()
    correct = 0
    with torch.no_grad():
        for i in range(0, len(aa), batch_size):
            logits = model(aa[i : i + batch_size], bb[i : i + batch_size])
            pred = logits.argmax(dim=-1)
            correct += (pred == labels[i : i + batch_size]).sum().item()
    model.train()
    return correct / len(aa)


def train_one_seed(
    p,
    seed,
    weight_decay,
    steps,
    device,
    frac_train=0.5,
    lr=1e-3,
    num_threads=None,
    log_every=100,
):
    """Trains one model for one seed. Returns a dict with the accuracy
    trajectory and whether grokking was observed under the pre-registered
    operational definition (held-out accuracy crosses 90% after train
    accuracy has already been >99% for >=500 steps)."""
    if num_threads is not None:
        torch.set_num_threads(num_threads)
    torch.manual_seed(seed)

    aa, bb, labels = make_dataset(p, device)
    (train_a, train_b, train_y), (test_a, test_b, test_y) = split_dataset(
        aa, bb, labels, frac_train, seed, device
    )

    model = GrokkingTransformer(p).to(device)
    opt = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=weight_decay, betas=(0.9, 0.98))

    train_accs, test_accs = [], []
    train_saturated_since = None
    grokked_at_step = None

    for step in range(steps):
        opt.zero_grad()
        logits = model(train_a, train_b)
        loss = F.cross_entropy(logits, train_y)
        loss.backward()
        opt.step()

        if step % log_every == 0 or step == steps - 1:
            tr_acc = accuracy(model, train_a, train_b, train_y)
            te_acc = accuracy(model, test_a, test_b, test_y)
            train_accs.append((step, tr_acc))
            test_accs.append((step, te_acc))

            if tr_acc > 0.99:
                if train_saturated_since is None:
                    train_saturated_since = step
            else:
                train_saturated_since = None

            if (
                grokked_at_step is None
                and te_acc > 0.90
                and train_saturated_since is not None
                and (step - train_saturated_since) >= 500
            ):
                grokked_at_step = step

    return dict(
        seed=seed,
        weight_decay=weight_decay,
        p=p,
        steps=steps,
        frac_train=frac_train,
        device=str(device),
        num_threads=torch.get_num_threads(),
        train_accs=train_accs,
        test_accs=test_accs,
        grokked=grokked_at_step is not None,
        grokked_at_step=grokked_at_step,
        final_train_acc=train_accs[-1][1],
        final_test_acc=test_accs[-1][1],
    )
