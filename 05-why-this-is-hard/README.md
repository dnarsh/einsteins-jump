# Why this is hard

## Where this picks up

By the time I got here, I'd already built and run two versions of a test for
whether a panel of AI judges could tell a genuinely new idea apart from an old
one wearing a disguise. Both times, the same failure mode showed up. The first
version got fooled outright — every judge on the panel, six for six, rated a
dressed-up, disguised version of a known idea as novel. The second version
tightened the screws, used harder test items, and still didn't hold up cleanly
enough to trust.

At that point I had a choice. I could keep patching the test — sharper
prompts, harder items, a better rubric — and hope the third or fourth version
finally worked. Or I could stop and ask a more basic question: is this
actually fixable with a better test design, or is there something structural
in the way?

So I stepped back from "how do I build a test that works" and asked instead:
has *anyone*, in any field, ever solved the underlying problem — certifying
that an idea is genuinely novel *and* correct, without already having an
answer key for it? Not "has anyone built a good novelty detector." The
narrower, harder question: does a method exist, anywhere, for scoring a
hypothesis as both unprecedented and right, when by definition nobody wrote
down in advance what "right" looks like?

That question is worth pausing on, because the trap is built into how it's
phrased. To grade a test, you need a pre-known correct answer. But a
pre-knowable correct answer is, by construction, a recognizable *type* of
idea — which is exactly why my first test got fooled. An idea that fits a
template you can write an answer key for is, almost tautologically, not a
genuinely unprecedented idea. A truly unprecedented idea has no answer key
that can exist in advance, because writing that answer key requires already
having had the idea.

That's the structural wall. The rest of this writeup is what happened when I
went looking for a way around it — first across a wide spread of fields that
might plausibly have solved it, then, after that came up empty, one level
deeper into philosophy, where it turns out this exact shape of problem has
been sitting unresolved for a very long time.

## The search: nine fields, then four more

I ran this in two waves. The first wave picked fields close to the AI/ML
world where I expected either an answer or a well-known reason there isn't
one. The second wave deliberately broadened out to fields with no shared
vocabulary or context with the first — the point being that if independent
fields, searched separately, all hit the same wall, that's much stronger
evidence than one field failing once.

**Wave one:**

- **Evaluating AI-generated text and ideas for novelty.** The methods that
  claim to be "reference-free" are only reference-free with respect to
  copying — they still assume some standard of what counts as novel exists
  somewhere. A directly-checked 2026 study (the "novelty mirage" paper) found
  that AI judges rate almost everything as highly novel, while the human
  experts evaluating the same material sharply disagree. Using an AI judge to
  score novelty is not currently a working method — it's a documented failure
  mode.
- **AI doing real science** (systems like DeepMind's Co-Scientist, Sakana
  AI's "AI Scientist"). The only mechanism anywhere that actually works is
  deferred confirmation: you let the idea sit until someone runs a real
  experiment and finds out, later, whether it was right. That's not a
  solution to the scoring problem — it's a way of avoiding having to solve it
  at the moment the idea is generated, and it only works when a real
  experiment is available to run. DeepMind's own CEO said plainly, on the
  record, that today's systems can't generate genuinely new hypotheses yet —
  five to ten years out, in his estimate.
- **Computational creativity.** The statistical tools here measure how far an
  idea sits from a reference corpus — rarity, not correctness. A separate
  technique (getting a panel of judges to rate creativity by consensus,
  without a rubric) just substitutes the judges' own internalized prior
  knowledge for a written answer key. It's still pattern-matching against
  what's already known; it's just distributed across more people.
- **Mechanism design without a ground truth** (the branch of game theory
  concerned with scoring people's answers when nobody, including the
  scorer, knows the right one). The best method here — peer prediction,
  verified directly against the current research — needs at least three
  independent respondents being cross-checked against each other. It
  structurally cannot evaluate one isolated idea from one source. And even
  where it's used, panels of judges have been shown to collapse toward the
  same correlated mistakes rather than independently catching each other's
  errors — the same shared-blind-spot problem I'd already found in miniature
  with my own judge panel.
- **Open-endedness and novelty-search research**, plus a handful of recent
  systems built specifically to evaluate AI-generated research ideas. Novelty
  search scores how far a new output sits from an archive of past outputs —
  again, distance, not correctness. The newer idea-evaluation systems either
  require comparing against existing literature (which defeats the purpose
  for something genuinely new) or explicitly say correctness evaluation is
  out of scope. The one real test I found that grounded novelty in an actual
  outcome — a 2026 project called HindSight, which had frontier AI systems
  attempt genuinely unpublished open research questions and had the actual
  paper authors grade the results — found the systems made no real progress.
  Grounding a test in a real-world outcome works, in principle. Current
  systems fail it.

**Wave two**, chosen deliberately to use each field's own native vocabulary
rather than my framing, so it wouldn't just find the same sources again:

- **Philosophy of science.** This is where the problem turns out to already
  be a named, mainstream position — not something I'd stumbled onto myself.
  The classic split between the "context of discovery" and the "context of
  justification" (Reichenbach), and Karl Popper's own position that there is
  no logic of discovery, only of testing, are both built on the premise that
  the moment of having a new idea isn't a rule-governed, formalizable step at
  all. Peirce — the philosopher who coined "abduction" for the act of
  generating a new explanatory guess in the first place — offered a way to
  rank guesses by plausibility once you have them, not a way to certify one
  as both new and correct. A 2025 survey of AI-driven scientific discovery
  restates the identical gap, for AI systems specifically, as still open.
- **Patent law.** Genuinely instructive, because it shows how an entire
  functioning legal and economic system handles this problem: it doesn't
  solve it, it relocates it. A patent examiner only ever certifies *absence
  from prior art* — nobody has published this exact thing before — never
  whether it actually works. A patent can be granted for something that
  doesn't function. Separately, "hindsight bias" — examiners unconsciously
  reconstructing a path to an invention as obvious only after they already
  know the answer — is a well-documented, unresolved problem in that
  multi-billion-dollar-a-year system. It's the mirror image of my own
  judges-fooled-by-a-disguised-retrieval finding.
- **Qualitative research methods** (grounded theory and similar). The
  standard safeguards here — comparing cases systematically, actively
  hunting for exceptions, having multiple researchers code the same data and
  checking agreement — are described candidly, by the methodologists who
  built them, as substituting documented *rigor of process* for a provable
  answer. They don't claim to solve the circularity; they manage it.
- **Mathematics.** This is the one field with a real, partial exception — and
  it independently arrived at almost exactly my own question, from a
  completely different direction. Formal proof verification lets a genuinely
  novel proof get certified as correct without a human-written answer key —
  a computer can check the logic mechanically. But mathematicians have
  already formalized the harder, adjacent question I was actually asking, in
  what's called the Birch test: does a system (1) make a discovery
  automatically, with no human steering, (2) surface a real, concrete
  structure, and (3) is that structure important enough to matter — in
  other words, does the system both *pose* and *certify* a genuinely novel
  result, entirely unassisted. As of the most recent survey, no AI system has
  passed it. The closest attempt got two of the three conditions but failed
  the "unassisted" part — humans were the ones who spotted the pattern
  inside the model, not the model itself. Even a celebrated 2026 case where
  an AI supplied a disproof of an 80-year-old conjecture in combinatorial
  geometry only supplied the counterexample; a human had posed the original
  conjecture, and humans did the work of recognizing and writing up what the
  disproof meant. Formal verification is a real escape hatch for
  *correctness* — but it doesn't generalize past domains you can fully
  formalize in symbols, and even there, it never touches the harder half of
  the problem: where the novel idea comes from in the first place.

Nine fields — evaluation methods for AI-generated text, AI-for-science,
computational creativity, mechanism design, open-endedness research,
philosophy of science, patent law, qualitative methodology, and mathematics —
and not one of them had an operational way to certify genuine novelty and
correctness together without either quietly moving the answer key somewhere
else (a reference corpus, a judge's own prior knowledge, a later real-world
experiment) or swapping in an easier claim that sounds similar but isn't
(surface-level novelty, absence from prior art, agreement among raters).
Several of these fields treat this as a live, explicitly acknowledged open
problem in their own current work — not something they consider solved.

That's a strong pattern. It isn't a proof. Nine independent fields failing to
find a solution is convergent evidence, not a mathematical impossibility
result, and I want to be honest about the difference — which is exactly why I
kept going one level deeper instead of stopping there.

## One level deeper: where this problem actually comes from

I went back in with one specific, falsifiable prediction: that anything I
found from here on would turn out to be a *philosophical dissolution* of the
problem — either denying the premise or declaring the target impossible to
formalize — rather than an actual operational fix. That prediction held, four
times out of four.

**Fodor's paradox of concept acquisition (1975).** This turned out to be the
closest known relative of the problem I'd been circling. The philosopher
Jerry Fodor pointed out something uncomfortable about how we think concept
learning works: the standard account is that you learn a new concept by
forming and testing hypotheses about it ("is this thing an X?"). But to even
*state* that hypothesis, you already need to possess the concept X. For a
genuinely primitive concept — one that isn't just built out of simpler
concepts you already have — that's circular. You can't hypothesis-test your
way into having a concept you need in order to form the hypothesis in the
first place. Fodor's own conclusion was stark: such concepts can't be
*learned* at all in any ordinary sense. They must be innate, and merely
*triggered* by experience rather than built up from it.

This is genuinely, structurally the same shape as the problem I'd been
searching for a solution to, not just a loose analogy. A judge that could
recognize a genuinely novel idea when it saw one would already need to
possess whatever category that idea belongs to — but if the judge already
has that category, the idea isn't novel to the judge. It's the identical
knot, just moved from an individual mind learning a concept to an external
judge scoring one. This isn't a fringe position, either — it's described in
the philosophy-of-mind literature as comparable in importance to two of the
other classic problems in that field (Quine's and Goodman's puzzles about
induction), and it stood largely unchallenged for over twenty years.

There is one honest place where the analogy isn't perfect, and it's worth
being precise about it: Fodor's own argument supplies an escape hatch for his
version of the problem — a concept can be "triggered" by raw causal exposure
with no judgment or evaluation involved, which sidesteps the circularity
because nothing is being *certified*, just switched on. A verifier doesn't
get that escape. Certifying an idea as novel-and-correct is inherently an
evaluative act — there's no equivalent non-evaluative "triggering" available
to a judge. So the two problems share a structure, but Fodor's has a way out
that mine doesn't.

**The same shape shows up again in developmental psychology.** A related
argument (Bereiter, 1985, building explicitly on Fodor, later extended by
Pascual-Leone) makes the same point about learning any *richer* cognitive
structure in general: explaining how a mind acquires a genuinely more
sophisticated structure than what it started with tends to require assuming
the mind already had something at least as sophisticated to begin with — or
the step from simpler to richer is unmotivated and circular. Every proposed
fix that's been offered for this — self-organizing systems, the idea that
richer structure gets "internalized" from social interaction, staged
maturation — is flagged candidly, by the field's own methodologists, as
*routing around* the problem rather than solving it. It's the same trap I'd
already run into from the AI-creativity-research side: what looks like
generating something structurally new is very hard to distinguish from
recombining things you already had.

**Then the ancient version: Meno's paradox**, from Plato, roughly 2,400 years
old. Plato has a character state it almost exactly: you cannot search for
something you already know, because you already know it — and you cannot
search for something you don't know, because you won't recognize it even if
you stumble onto it. Plato's own answer — the theory that the soul already
knew everything before birth and learning is just remembering — doesn't
actually dissolve the paradox. It *concedes* the premise (you do need to
already know it) and just relocates the "already knowing" into a past life
where you can't check it. Every modern response to Meno's paradox I found
does a version of the same move: weaken "knowing" down to "partial
foreknowledge — just enough to recognize the right answer without being able
to produce it yourself." That's not an escape from needing an answer key. It's
a smaller, blurrier answer key. Twenty-four centuries of serious attention
from professional philosophers has produced better-dressed versions of the
same concession, not an operational way out. Of everything I found, this is
the cleanest illustration of a pattern that kept recurring across every field
I searched: an apparent "solution" that, on inspection, just moves the answer
key somewhere less visible instead of removing the need for one.

**And finally, the two real historical attempts to actually build a machine
that discovers things — both of which fail for the identical structural
reason.** The logician Jaakko Hintikka built a formal "logic of discovery"
specifically to answer Popper's claim that no such logic could exist — a kind
of structured question-and-answer game against nature. It works, but only
because it assumes nature is a well-defined oracle answering from a space of
possible answers that's already been laid out in advance. That's a real logic
of *strategy* for searching a known space — not a way to generate genuinely
new categories of answer that didn't previously exist in that space. And
BACON, the AI program from the 1970s and 80s famous for "rediscovering"
scientific laws like Kepler's third law and Boyle's law purely from raw data,
has a long-standing, still-unrebutted critique behind it: it was curve-fitting
relationships between variables that human scientists had already selected,
cleaned, and framed as the relevant ones to look at. It never had to decide
*which* variables mattered or reframe the problem itself — humans did that
part before BACON ever started. Current commentary on today's AI-for-science
systems restates this exact same critique, in modern language, as still
applying.

## What this does and doesn't establish

Thirteen independent fields, now — evaluation methods for generated text,
AI-for-science, computational creativity, mechanism design, open-endedness
research, philosophy of science, patent law, qualitative methodology,
mathematics, philosophy of mind, developmental psychology, classical
epistemology, and the two real historical attempts to mechanize discovery
itself — and every single one converges on the same shape of wall. Any
proposed fix either quietly relocates the answer key (to a corpus, to a
judge's own prior knowledge, to a later real experiment, to a past life) or
ends up answering a different, easier question than the one that actually
matters (surface novelty, absence from prior art, rater agreement, rigor of
process).

I want to be precise about what that does and doesn't prove. It does not
prove this is formally, mathematically impossible. Even Fodor's own
conclusion — that primitive concepts must be innate rather than learned — is
a considered philosophical position, not a theorem, and it's still being
actively contested (a 2025 paper tries seriously to dissolve the nativist
conclusion specifically). What thirteen fields failing to find an escape
*does* establish is a strong, convergent, cross-disciplinary pattern: this is
one of the oldest, most worked-over, least-resolved structural problems in
the relevant span of human inquiry — not a gap specific to what I personally
had the resources to try, and not something anyone, in any field, currently
has an operational answer for.

The one genuine, partial escape route that exists anywhere is deferred
validation against a real experiment — proposing something and then actually
waiting for the real world to confirm or refute it, the way DeepMind's
Co-Scientist and similar systems operate. That's a real way around the
problem. It's just not available to a solo project working with free compute
and no lab: it requires a genuine open scientific question and the ability to
go run a real experiment against it, which is squarely the kind of resource
that separates an institutionally funded lab from someone doing this on
their own time. So the honest conclusion isn't "AI novelty-detection is
impossible forever." It's narrower and, I think, more useful: no cheap,
accessible way to build and test it exists right now, and the one real way
out that anyone has found requires resources this project never had.

## A smaller side test: the temporal holdout pilot

Alongside all of this, I ran one more small, separate experiment, because I
wanted to see something directly rather than just take the reasoning above on
faith.

The idea: find a real scientific discovery, recent enough that an AI model
almost certainly hadn't seen it during training, describe only the
*unexplained puzzle* that came before the discovery — with the actual
resolution withheld — and see what the model proposed. I picked a case that
was real, well-documented, recent, and self-contained enough to describe
without accidentally leaking the answer: a genuine mystery about Saturn's
measured rotation rate, resolved in March 2026 using JWST data and published
in a peer-reviewed space-physics journal. Since 2004, Saturn's measured
rotation period had appeared to drift depending on when and how it was
tracked — puzzling, because a planet's actual bulk spin shouldn't simply
speed up or slow down year to year. It went unexplained for roughly two
decades.

Before running it, I wrote down what each possible outcome would actually
mean — on purpose, before seeing the result, so I couldn't quietly reinterpret
it afterward. A match to the real answer would *not* count as evidence of
genuine novel reasoning. The far more likely explanation for a match would be
that the answer was reachable through ordinary, strong scientific reasoning
applied to the puzzle as stated — not evidence of an unprecedented leap. A
miss was the expected, predicted outcome, consistent with everything else
this investigation had found.

What actually happened: no match — the predicted result — but with a texture
worth reporting honestly rather than filing away as a flat null. Instead of
the real answer (a self-sustaining loop of auroral heating and
upper-atmosphere winds that mimics a variable spin signal), the model
proposed something else entirely: that the "rotation period" being tracked
was never the planet's actual bulk spin at all, but the periodicity of a
specific magnetospheric radio signal that drifts for unrelated plasma-physics
reasons — and it backed that up by citing a real, correct, independent
mechanism (a 2019 study using Saturn's ring structure to measure the true
interior rotation rate) as how scientists eventually got around the radio
signal's drift.

That's not a random or confused guess. It's a real, specific, correct account
of a related — but different — piece of Saturn science, complete with a named
mechanism and a named paper. Read plainly, this looks like recall of real
prior knowledge about a closely related question, not confused guessing, and
not, as far as one small test like this can tell, genuine engagement with an
unprecedented puzzle. That's exactly the distinction this entire
investigation kept circling back to: it's very hard to tell "the model
reasoned its way to something new" apart from "the model found something
adjacent it already knew and reached for that instead." One honest loose end
I couldn't resolve within this small test: whether the 2026 finding and the
2019 mechanism the model cited are competing explanations, complementary
pieces of the same picture, or sequential steps in the same research
story — that's a real astrophysics question this pilot wasn't built to
settle.

This was one case, run once. It doesn't prove anything on its own, and I'm
not treating it as if it does. What it adds to everything above is a small,
concrete picture of the exact distinction the whole search kept running
into — reaching for something real and adjacent that's already known is not
the same thing as generating something that wasn't there before, and from the
outside, the two can look remarkably alike.
