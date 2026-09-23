"""
Component checks (forced-fail baseline, positive control), run before the
full 5-seed sweep. Both must pass before the main run counts for anything --
see the README for why.
"""
import torch
from grokking_harness import train_one_seed

P = 97
STEPS = 10000
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
NUM_THREADS = 4

print(f"device={DEVICE}, num_threads pinned={NUM_THREADS}")

print("\n=== Forced-fail baseline: weight_decay=0, must NOT grok ===")
result_fail = train_one_seed(
    p=P, seed=0, weight_decay=0.0, steps=STEPS, device=DEVICE, num_threads=NUM_THREADS
)
print(f"final_train_acc={result_fail['final_train_acc']:.4f} "
      f"final_test_acc={result_fail['final_test_acc']:.4f} "
      f"grokked={result_fail['grokked']}")
forced_fail_ok = not result_fail["grokked"]
print(f"[{'PASS' if forced_fail_ok else 'FAIL'}] forced-fail baseline "
      f"{'did not grok, as expected' if forced_fail_ok else 'GROKKED -- harness/checker is broken, stop and fix'}")

print("\n=== Positive control: weight_decay=1.0 (Omnigrok range), must grok ===")
result_pos = train_one_seed(
    p=P, seed=0, weight_decay=1.0, steps=STEPS, device=DEVICE, num_threads=NUM_THREADS
)
print(f"final_train_acc={result_pos['final_train_acc']:.4f} "
      f"final_test_acc={result_pos['final_test_acc']:.4f} "
      f"grokked={result_pos['grokked']} grokked_at_step={result_pos['grokked_at_step']}")
positive_control_ok = result_pos["grokked"]
print(f"[{'PASS' if positive_control_ok else 'FAIL'}] positive control "
      f"{'grokked, as expected' if positive_control_ok else 'DID NOT GROK -- harness cannot be trusted for the main run'}")

print(f"\n{'BOTH CHECKS PASS -- proceed to main sweep' if (forced_fail_ok and positive_control_ok) else 'CHECK(S) FAILED -- do not run the main sweep, fix the harness first'}")
