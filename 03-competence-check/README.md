# A competence check: replicating a known result before trusting my own methodology

Everything else in this repo is about a genuinely open question — can you
tell whether an AI invented something new, or just recombined something it
already knew? Before spending real effort on that question, I wanted proof
that I could actually run a rigorous experiment correctly, end to end, on
real compute, against something with a known right answer. Not a novel
claim. Not a finding. A sanity check on my own process, using a result
someone else had already published, so there was no ambiguity about
whether I was fooling myself.

The result I picked: **grokking** — a well-documented phenomenon where a
small neural network trained on a simple arithmetic task appears to
memorize the training data early on, plateaus, and then, well after
training accuracy has already saturated, suddenly jumps to generalizing
correctly on held-out examples it's never seen. It's a real, published,
reproducible effect, first named in a 2022 OpenAI paper, and it's small
enough to run on a laptop GPU in minutes. Perfect for what I needed: a
target with a known, checkable answer, not something where I'd have to
trust my own judgment about whether the result "counted."

## Why I copied someone else's exact setup instead of designing my own

I specifically picked a recent paper — "Grokking Is Conditional and
Fragile: A Fully-Tractable, Multi-Seed Study at 12K Parameters" (Ootani,
2026) — and replicated its actual setup directly, rather than building my
own bespoke version of a grokking task. That was a deliberate choice: if I
built my own variant, there'd always be a nagging question of whether any
interesting result was "secretly novel" or just an artifact of my own
design choices. Copying a known paper's methodology exactly removes that
ambiguity entirely — any result is either a clean replication or a clear
deviation, nothing in between.

It also meant I could adopt the paper's own hard-won lessons about how
single-run grokking studies fool themselves, rather than rediscovering
those lessons the hard way myself:

1. **Track a grok rate across multiple seeds, not one run.** The paper's
   central methodological point is that a single seed's grok-or-no-grok
   outcome is closer to noise than signal — you need a rate across several
   independent seeds to say anything real.
2. **Pin the numerical environment and report it.** The paper found that
   CPU thread count, and CPU-versus-GPU execution, each flip a minority of
   same-seed outcomes with no detectable shift in the aggregate rate — a
   "numerical knife-edge." So I fixed the device and thread count up front
   and reported both alongside every result, rather than treating them as
   incidental details.
3. **Use the known weight-decay effect as a positive control.** Before
   trusting any result from my own harness, I needed to confirm it could
   reproduce an already-established easy case.
4. **Use a no-weight-decay run as a forced-fail baseline.** A model with no
   weight decay should not grok. If it does, something is wrong with the
   harness or the scoring logic, not with the concept of grokking.

## Setup

- **Task:** modular addition, `(a + b) mod p` — the standard benchmark task
  for this kind of study.
- **Modulus:** p = 97, matching the faster-grokking configuration used in
  well-known minibatch replications of this task (as opposed to the older,
  slower full-batch p = 113 setup), chosen to keep the compute budget
  small — disclosed here rather than left implicit.
- **Architecture:** a standard, minimal reference implementation — a
  2-layer, decoder-only transformer, the pattern widely used in grokking
  reproductions, not something I hand-rolled myself. That choice was
  deliberate: a bug in a hand-rolled architecture could easily masquerade
  as "no grokking occurred," and I wanted to rule that failure mode out
  from the start.
- **Optimizer:** AdamW, with weight decay as the manipulated variable — 0.0
  for the forced-fail baseline, and a value from the known "Omnigrok"
  weight-decay literature (1.0) for the positive control and the main run.
- **Device:** a single consumer GPU (RTX 5060 Laptop, 8.5GB VRAM), CPU
  thread count pinned to a fixed value, both reported with every result.
- **Train/held-out split:** the standard grokking split — roughly half of
  all possible `(a, b)` pairs used for training, the rest held out entirely.
- **Metric:** train accuracy and held-out accuracy, checked every 100
  steps. "Grokked" is defined the standard way — held-out accuracy crosses
  90% only after train accuracy has already been above 99% for at least
  500 steps, ruling out a case where both just happen to cross around the
  same time by coincidence.

## What I fixed in place before running anything

- 10,000 training steps per seed — comfortably past the ~4,000-step point
  where the faster minibatch replication I was matching typically groks,
  with margin, and well under the slower canonical setup's 40,000-step
  runs. On this GPU, that's minutes, not the much longer CPU budget I'd
  originally scoped before I had GPU access.
- A minimum of 5 independent seeds, to get a real grok rate rather than a
  single data point.
- The plan itself: run the two component checks first (forced-fail
  baseline, positive control). Only if both behaved as expected would I
  run the full 5-seed sweep. Report the grok rate across seeds, compared
  honestly to the source paper's own findings. No extending the run or
  changing the definition of success after seeing any results.
- Explicitly out of scope: this was not going to become a claim of any
  kind, novel or otherwise, regardless of what the numbers showed. If
  anything came out looking interesting, the plan was to report it
  plainly as an observation, not quietly reframe it into a bigger claim.

## Component checks (both had to pass before the real run counted for anything)

| Check | Weight decay | Result | Verdict |
|---|---|---|---|
| Forced-fail baseline | 0.0 | train accuracy 1.0000, held-out accuracy 0.0281 (chance is about 1/97 ≈ 1.03%) — did not grok | Pass — the harness correctly tells memorization apart from generalization |
| Positive control | 1.0 | train accuracy 1.0000, held-out accuracy 1.0000, grokked at step 2,300 | Pass — the harness reproduces the known, easy weight-decay effect |

Both passed, so the main 5-seed sweep went ahead as planned.

## Main result: 5-seed grok rate

p = 97, weight decay = 1.0, half the pairs used for training, 10,000 steps,
GPU, thread count pinned to 4, seeds 0 through 4:

| Seed | Grokked | Step | Final held-out accuracy |
|---|---|---|---|
| 0 | Yes | 2,900 | 1.0000 |
| 1 | Yes | 2,700 | 1.0000 |
| 2 | Yes | 1,700 | 1.0000 |
| 3 | Yes | 1,800 | 1.0000 |
| 4 | Yes | 2,300 | 1.0000 |

**Grok rate: 5 out of 5.** The step at which grokking happened varied
meaningfully across seeds — mean around step 2,280, ranging from 1,700 to
2,900, a real spread of about 1,200 steps in *when* it happened, even
though *whether* it happened was unanimous.

## Honestly comparing this to the paper I replicated

The paper's headline finding is that grokking is conditional and fragile —
gated by how much of the input space the training set covers, with a
numerical knife-edge where thread count and CPU-versus-GPU execution flip
a minority of individual outcomes. This run found none of that fragility:
5 out of 5, clean, comfortably inside the compute budget.

That is not a contradiction of the paper's finding, and I'm not reporting
it as one. The most likely explanation, stated plainly: this run used one
single, fixed configuration — half the data for training, weight decay at
1.0 — that sits well inside a reliable region of the parameter space, not
anywhere near the coverage threshold or the borderline weight-decay values
where the paper's fragility result actually shows up. A 100% grok rate
here is consistent with what the paper predicts for a configuration deep
inside the reliable regime — it isn't in tension with their result, because
this exercise never probed the boundary they were characterizing. To be
specific about what wasn't tested: this run never varied the training-set
fraction or the weight decay across the sweep, so there's no data here
that speaks to their coverage-threshold question either way.

I want to be direct about the temptation this kind of clean result
creates: it would be easy to spin "my replication came out cleaner than
the original paper" into some kind of finding. It isn't one. This is a
successful replication of the reliable-regime behavior the paper itself
predicts, using methodology adopted directly from that paper — a
multi-seed rate instead of a single run, a pinned numerical environment, a
known positive control — nothing more than that.

## What this actually demonstrated

1. My own experimental process — pre-register the plan, run a forced-fail
   check, run a positive control, only then run the real sweep — works
   end to end on a real, GPU-accelerated training run, not just on paper.
2. The lessons I adopted from the paper (multi-seed rate over a single
   run, a pinned numerical environment, a known-easy positive control) are
   now something I've actually executed, not just read about.
3. My original compute budget for this — CPU-only, single seed, a fairly
   short time cap, planned before I had GPU access — would have been
   underpowered even for this simple case. The budget I actually used
   (10,000 steps times 5 seeds, on GPU) ran in minutes once I switched to
   the GPU, which confirmed that the earlier CPU-only plan really would
   have been a problem.

## What this did not do

- It did not probe the coverage-threshold fragility boundary the source
  paper is actually about — that would be a different, larger exercise,
  varying training-set fraction and/or weight decay across a grid instead
  of a single fixed point.
- It did not test CPU-versus-GPU numerical sensitivity, the paper's other
  named finding — this run used GPU only, at one fixed thread count.
- It was never meant to be, and isn't, a novel finding of any kind. It's a
  replication, used to validate my own process before applying that same
  process to the actual open question this repo is about.

Raw results are included in this folder: `code/main_sweep_results.json`
(the summary numbers) and `code/main_sweep_trajectories.json` (the full
train/held-out accuracy curves for all 5 seeds, logged every 100 steps).
The code that produced them is in `code/` as well — `grokking_harness.py`
(the model and training loop), `run_component_checks.py` (the forced-fail
and positive-control checks), and `run_main_sweep.py` (the 5-seed run
itself).
