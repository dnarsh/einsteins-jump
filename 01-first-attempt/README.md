# First attempt: does a disguised physics puzzle stay disguised?

This was the opening move in a side project I ran to see if you could build
a test that tells the difference between an AI genuinely inventing a new
idea and an AI quietly recombining something it already knows and dressing
it up to look new.

The instinct behind it: some of the most famous moments in the history of
science are "abductive leaps" — you're staring at data that doesn't add up,
and you resolve the contradiction by proposing something new. Pauli
proposing an invisible, undetected particle (the neutrino) to save
conservation of energy in 1930. Einstein deciding that two people who
disagree about whether two events happened "at the same time" can both be
right, because simultaneity itself isn't absolute. Both are the same basic
move: something you assumed was fixed turns out not to be, or something you
assumed didn't exist turns out to.

I wanted to know: if you build a brand-new, fictional version of that kind
of puzzle — new vocabulary, no physics words anywhere — can an AI actually
make that leap on its own? Or does it just pattern-match the shape of the
puzzle to a famous answer it already knows, and produce something that
*looks* like a fresh insight but is really retrieval wearing a costume?

## The puzzle I built

I made up a small fictional bookkeeping system — invented nouns like
"kites," "clasps," "braids," and a stated rule I called "the Tally Law"
(basically, a conservation law: some quantity has to balance out). Then I
built two anomalies that individually look like ordinary bookkeeping
errors, but together only make sense if you posit something new.

I tried two different ways of resolving the anomaly, because I wanted to
give the idea a fair shot before concluding anything:

- **Resolution A — a hidden thing.** The anomaly gets explained by positing
  a new, previously unmentioned, unobserved entity (I called it a "wisp")
  that's carrying the missing quantity. This is structurally identical to
  Pauli's neutrino move: numbers don't balance, so you invent something
  unseen that balances them.
- **Resolution B — a relative property.** Instead of inventing a new thing,
  this resolves the anomaly by taking a property everyone assumed was
  absolute and making it relative to the observer instead. This is
  structurally Einstein's move on simultaneity.

Before spending real effort building the full test apparatus around either
of these, I ran a cheap, fast check first: take the anomaly and its
resolution, written entirely in the made-up vocabulary — no physics words,
no hints — and show it to independent AI judges who'd never seen anything
else about the project. Ask them one question: "does the reasoning move
here remind you of any real scientific, historical, or philosophical idea,
and if so, name it." Nothing in the prompt mentioned physics, conservation,
Einstein, or Pauli.

## What happened

Three fresh judges per condition, each starting from a blank slate with
zero shared context between them.

- **Resolution A (hidden thing):** 3 out of 3 judges named the neutrino and
  Pauli's 1930 postulate, unprompted and explicitly. One judge also
  spontaneously brought up the discovery of Neptune via its gravitational
  effect on Uranus's orbit, as a structurally identical case.
- **Resolution B (relative property):** on the first pass, I'd accidentally
  written the setup in a way that described the two measurements as
  happening while "moving relative to one another" — which is literally
  the setup of special relativity, so that version leaked the answer before
  the resolution was even shown. I caught this, rewrote it to remove any
  motion/frame language, and reran it clean with three new judges. Result:
  3 out of 3 again named special relativity, explicitly and unprompted,
  even with the leading cue gone.

Put together: **6 out of 6 valid judges converged on an exact, named,
famous scientific reasoning template**, in both resolution styles, even
through invented vocabulary and after removing the one obvious leak I
found. Total cost of this check: about 9 model calls.

## What it means

This wasn't a finding about whether the AI *can* make abductive leaps. It
was a finding about whether this particular test could even ask that
question. It couldn't.

The underlying shape of the puzzle — a conservation/measurement anomaly
that gets resolved by revising an assumption about some quantity — is
itself a physics-shaped problem. Dressing it in nonsense words defeats
simple string-matching, but it doesn't defeat concept-level pattern
matching: the AI recognizes the *shape* of the problem, not the specific
words, and the shape alone is enough to summon the famous answer. Any
resolution I could plausibly write for this kind of puzzle was going to
land close to something already sitting in the training data, because the
whole reason these are famous scientific moves is that they're natural,
recognizable patterns — that's precisely why they got famous in the first
place.

I considered trying a third or fourth resolution style specifically
engineered to avoid every well-known template. I decided against it: if
you deliberately search for a resolution style with no recognizable
analogy, you risk landing on something that also isn't a genuine abductive
move anymore — you'd just be gaming the test, not fixing it. That's not a
result, that's fishing for one.

So this was a real structural wall, found cheaply — for about 9 calls —
before I'd built any of the larger test rig this idea would have needed
(a full run would have cost somewhere between 110 and 420 model calls
depending on scale). The domain itself couldn't separate "the AI genuinely
reasoned its way to something new" from "the AI recognized a famous pattern
and reskinned it," no matter how well I built the rest of the apparatus
around it. That's the honest, if unglamorous, result of attempt one: not a
capability failure, but a test-design dead end, caught before it got
expensive.

The one thing worth keeping from this: it's genuinely interesting, on its
own, that a synthetic anomaly built specifically to *avoid* being
recognizable still converged unanimously on famous answers, twice, even
after removing an obvious leak. That's a real, if narrow, data point about
how good these models are at concept-level analogy retrieval — just not
the data point I originally set out to collect.
