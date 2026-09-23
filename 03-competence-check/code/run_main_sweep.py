"""
Main 5-seed sweep. Only run after both component checks pass -- see
run_component_checks.py. Reports grok rate across seeds (the multi-seed-rate
methodology this whole exercise adopted from Ootani 2026, arXiv:2607.05104),
not a single boolean outcome.
"""
import json
import torch
from grokking_harness import train_one_seed

P = 97
STEPS = 10000
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
NUM_THREADS = 4
WEIGHT_DECAY = 1.0  # positive-control value, matches run_component_checks.py
SEEDS = [0, 1, 2, 3, 4]

print(f"device={DEVICE}, num_threads pinned={NUM_THREADS}, weight_decay={WEIGHT_DECAY}, "
      f"p={P}, steps={STEPS}, seeds={SEEDS}")

results = []
for seed in SEEDS:
    print(f"\n=== seed={seed} ===")
    r = train_one_seed(
        p=P, seed=seed, weight_decay=WEIGHT_DECAY, steps=STEPS,
        device=DEVICE, num_threads=NUM_THREADS,
    )
    print(f"final_train_acc={r['final_train_acc']:.4f} final_test_acc={r['final_test_acc']:.4f} "
          f"grokked={r['grokked']} grokked_at_step={r['grokked_at_step']}")
    results.append(r)

grok_rate = sum(1 for r in results if r["grokked"]) / len(results)
print(f"\n=== SUMMARY ===")
print(f"grok rate across {len(SEEDS)} seeds: {grok_rate:.2f} ({sum(1 for r in results if r['grokked'])}/{len(SEEDS)})")
for r in results:
    print(f"  seed={r['seed']}: grokked={r['grokked']} at_step={r['grokked_at_step']} "
          f"final_test_acc={r['final_test_acc']:.4f}")

with open("main_sweep_results.json", "w") as f:
    json.dump(
        [{k: v for k, v in r.items() if k not in ("train_accs", "test_accs")} for r in results],
        f, indent=2,
    )
    # accuracy trajectories saved separately, they're large
with open("main_sweep_trajectories.json", "w") as f:
    json.dump(
        {str(r["seed"]): {"train_accs": r["train_accs"], "test_accs": r["test_accs"]} for r in results},
        f, indent=2,
    )

print("\nResults written to main_sweep_results.json, main_sweep_trajectories.json")
