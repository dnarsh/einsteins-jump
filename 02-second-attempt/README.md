# Second attempt: can it find the right answer but still not pick it?

The first attempt hit a wall: any puzzle shaped like a real conservation
anomaly tends to resolve to a famous physics answer already sitting in an
AI's training data, no matter how you disguise the vocabulary. That wall
was structural, not something I could design around. So I moved to a
different question that didn't depend on avoiding famous patterns at all.

The new idea: maybe the interesting gap isn't "can the AI invent something
genuinely new," but "can the AI even correctly use an idea it clearly
already has." Specifically — if you let a model brainstorm freely, does the
right answer show up in its own list of guesses? And if it does, does
forcing the model to pick one answer from a fixed multiple-choice list
actually make it *worse* at landing on that same right answer? If
generation and forced-choice selection behave differently, that gap itself
would be worth understanding, separately from any question about genuine
novelty.

## The test shape

I built small riddles in what I ended up calling a "category-boundary
reframe" family: a short scene where something ordinary gets mistaken for
something else, because of a shared surface resemblance, plus one quiet
detail that only the true answer actually explains. A boulder mistaken for
a crouching wolf, except it hasn't moved position in three years even
though the flock keeps getting rotated to different pastures. A
weathervane mistaken for a bird, except it swivels to face the wind
exactly on cue. That kind of thing.

Each item ran in three separate conditions, each in a completely fresh,
independent conversation so nothing could leak from one condition to
another:

- **Generation:** given just the scene, list up to 8 possible answers,
  ranked most to least likely, no candidate list shown.
- **Baseline verification:** given the scene plus a 5-option list (the
  right answer, the "lure" — the thing it superficially resembles — and
  three unrelated filler options), answer with just one word.
- Two more verification variants layered on top of that baseline: one that
  explicitly instructs the model to check each candidate against the
  decisive clue one at a time before answering, and one that asks for an
  initial answer and then explicitly prompts "did you account for the
  decisive clue? reconsider if needed."

Every answer was scored by exact string match against a predefined correct
word — no AI judge grading "was this good," just a mechanical check.

I also built in two sanity checks from the start: a trivially easy
positive-control question (a red car in a driveway, described in a way
that should be unmissable) that any working setup should get right nearly
100% of the time, and a "forced-fail" version of one item with the correct
answer removed from the list entirely, to see whether the model would
correctly say "none of these" when that was the honest answer.

## Calibrating before running the real thing

Before spending the larger budget on the real pilot, I ran a small
calibration check first — three items, checking whether the test apparatus
was actually sensitive enough to detect anything. The logic: if models
already get the forced-choice question right nearly 100% of the time, the
test is dead on arrival — there's no room left for a generation-versus-
verification gap to show up, whether or not that gap is real. The
pre-registered bar was: proceed to a full pilot only if the generation
success rate cleared 60% and the baseline-verification rate stayed at or
below 70%.

That first three-item check came back at generation = 3/3 (100%) and
baseline verification = 2/3 (67%) — passed the gate, though narrowly (one
more correct answer would have failed it). Looking closer, though, two of
the three items were "inert" — the model got them both right cleanly with
no sign of struggle — so only one item out of three actually produced any
interesting behavior at all. On that one item, the model's free-form
brainstorm never actually generated the wrong answer it went on to pick
under forced choice; the planted multiple-choice list introduced a wrong
option the model's own generation hadn't proposed, and it picked that. Not
a clean "it knew the answer but failed to select it" story — messier than
that, and worth saying so plainly rather than rounding it up to a clean
result.

## The full pilot — and running into a ceiling

With the gate passed, I built six brand-new items (deliberately different
ones from the calibration set, so I wasn't fitting a story to data I'd
already seen) and ran the full three-condition pilot.

Every single condition came back at 6 out of 6: generation found the
correct answer in all six items, and baseline verification, structured
verification, and the reconsideration variant all scored 100% as well.

That's not a finding that verification is easy or that there's no gap —
it's the specific failure mode the calibration gate exists to catch.
Once baseline verification is already sitting at a perfect score, there's
no mathematical room left for a "generation beats verification" gap to
appear, regardless of whether the underlying effect is real. The gate had
passed on three *different* items than the six actually used in the full
run — the green light didn't transfer to the item set that mattered. That
mismatch, not any conclusion about the model's reasoning, was the real
result of this run: a calibration gate has to be tested on the exact items
you're about to use, not a proxy set you swap out afterward.

Two smaller things did come out of this run, worth recording honestly even
though neither was the headline result I was testing for:

- On two of the six items, when the model was asked for an initial answer
  before the "reconsider" nudge, that first-pass answer was the wrong,
  visually-similar option — even though a separately-run baseline call on
  the identical item got it right. Both self-corrected once explicitly
  asked to reconsider. Interesting, but it's a sample size of two from a
  side observation, not something I'd built the test to measure, so I'm
  flagging it rather than promoting it.
- The "forced-fail" control — the item with the correct answer deliberately
  removed from the list — was supposed to make the model say "none of the
  above." It didn't. It picked the option most consistent with the
  decisive clue among what remained, rather than the item's original
  surface lure, and rather than admitting no correct option was present.
  That's a real, useful thing to have learned: models under forced choice
  default to picking the least-bad option rather than volunteering "none
  of these," which means a "remove the right answer, expect NONE" control
  only works if you've separately confirmed the model will ever say NONE
  at all. I hadn't, so this control couldn't do the job I built it for —
  that's on the test design, not a sign anything else was broken.

## Trying again with harder items

The full pilot's problem was clear: the decisive clues I'd written were too
airtight — a single fact that flatly ruled out the wrong answer, so the
model never had to struggle. For the next attempt I built six new items
with deliberately subtler clues — details that suggest the right answer
without absolutely forcing it — and, having learned the lesson from the
mismatch above, I ran the calibration gate on these exact six items before
building anything further, not on a different proxy set.

Results: generation still found the correct answer on all six items, but
baseline verification came in at 5 out of 6 (83%), missing the
pre-registered ceiling requirement of 70% or below. The gate did not pass.
Per the plan I'd committed to before running it, that meant stopping there
— no full pilot on this item set, and no building a third item set to try
to squeeze through the gate.

The one real miss on this set (a decoy duck mistaken for a real duck) was
itself informative: the wrong answer the model picked wasn't the
constructed "lure" option and wasn't a near-miss of the right answer — it
was an unrelated third option from the list entirely. That's a different
error pattern than "got seduced by the obvious visual double," which was
the mechanism this whole design was built to detect and measure.

## Where this left things

Across three item sets — the original three-item calibration check, the
six-item full pilot, and the six-item harder-items attempt — baseline
verification landed at 67%, 100%, and 83% respectively. None of the three
sat cleanly inside the range needed to actually run and interpret the
comparison I was trying to make. Tuning item difficulty finely enough to
get a test with real discriminating power turned out to be its own
unsolved problem, separate from the actual question I was trying to
answer.

This is a different kind of wall than the first attempt's. The first one
was structural — the domain itself couldn't ask the question I wanted to
ask, no matter how well I built around it. This one is practical — the
question is still askable in principle, but I never landed on an item set
sharp enough to actually test it within the effort I was willing to put
into hand-tuning puzzle difficulty. If I revisit this, the honest next
step is clear: items with even subtler clues, validated on the exact set
used before any real run, and a forced-fail control that's first confirmed
to elicit "none of these" on at least one item where that's unambiguously
correct — because as it stands, that control couldn't tell me what it was
built to tell me either time I tried it.
