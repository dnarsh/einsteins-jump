# Building Apex: trying my hardest to break my own conclusion

By this point I'd already reached a fairly strong conclusion (see [why this is hard](../05-why-this-is-hard/)): distinguishing genuine novelty from disguised retrieval isn't something I could measure cheaply, and the reason traces to a real, old, unresolved problem in philosophy of mind. That's the kind of conclusion that's easy to talk yourself into too early. So instead of stopping there, I built the most adversarial version of a detector I could think of — I called it Apex — and spent a focused stretch trying explicitly to break my own conclusion with it. This is the record of that attempt: eight separate tests, run back to back, each one designed to give the conclusion its best chance to fail.

## What Apex actually is

Not one AI, several, playing different roles against the same claim:
- One or more judges with live web search, deliberately given different search habits from each other (so they're not just repeating the same query).
- A dedicated "disconfirmation-seeker" — a judge whose entire job is to argue the *opposite* of whatever the honest verdict looks like. If the claim looks novel, it has to argue it's actually a known idea in disguise. If a resolution looks like it matches a real theory, it has to argue as hard as it can that it doesn't.
- A way of combining these into one verdict.

The idea: if a single AI judge can be fooled by a disguised-but-actually-known idea, a panel with search diversity and a built-in adversary should catch what the lone judge misses. That's the hypothesis Apex exists to test.

## Test 1 — famous myths (a null, for a boring reason)

First stress test: give Apex and a lone judge four claims — three famous, thoroughly-debunked myths (Napoleon wasn't actually short for his era; the "Einstein failed math" myth; the Coriolis-effect bathtub-drain myth) and one true-but-surprising fact (lightning is hotter than the surface of the sun) — and see if the panel catches anything the lone judge doesn't.

Both scored 4 for 4, both above 95% confidence, both with clean citations. Zero difference. The reason turned out to be uninteresting in a useful way: these myths are debunked so thoroughly, by so many authoritative sources (encyclopedias, physics departments, fact-checking sites), that a single search reliably turns up the correction. The test never got to probe what it was actually meant to probe — a case where the *wrong* answer is what dominates search results — because I picked cases that were too easy for anyone.

## Test 2 — a properly graduated difficulty ladder

I tried again, deliberately building harder test cases: four claims varying exactly one thing — how easy the correction is to find, independent of how well-known the topic is. This included a real, documented case: a vitamin K2 supplement claim about preventing fractures, where the supporting research had been fabricated by a researcher whose fraud was later exposed (over a hundred retractions, among the largest cases in medical research), yet the fabricated conclusion had already been baked into official clinical guidelines before anyone caught it.

Every condition — the lone judge, two differently-configured panel judges, and the disconfirmation-seeker — reached the correct false verdict on every claim, including the fraud-guideline case. Zero separation on the metric I'd pre-registered (does the panel catch a false claim the lone judge misses). Another honest null, not a construction failure this time — I'd built a genuinely harder test and it still came back flat.

But I noticed something I hadn't pre-registered, so I could only note it as an informal observation rather than a real result: on the fraud case specifically, everyone's confidence dropped noticeably (70-85%, versus 95-99% on the other claims), and only one search approach actually surfaced *why* the claim was false — the others reached "false" through vaguer reasoning like "the evidence looks inconclusive," without ever finding the actual fraud. That's a different question than the one I'd tested — not "does the panel get the right verdict" but "does the panel understand the real reason" — and I didn't have a proper test for it yet. That loose thread is exactly what the [follow-up work](../07-followup-test-2026/) months later went back to close properly.

## Test 3 — pointing Apex at my own earlier failures

Next, I turned Apex on the exact puzzles from my [very first attempt](../01-first-attempt/) — the ones where a single judge recognized the disguised physics idea 6 times out of 6. This time using Apex's real search-based mechanism instead of a judge working from memory alone, plus a disconfirmation-seeker explicitly trying to argue the puzzles were genuinely novel.

Both puzzles got matched again — one to the neutrino postulate (92-98% confidence), one to special relativity — and the disconfirmation-seeker, whose entire job was to argue novelty, reported it "could not maintain the no-match position" on either one. A harder, more adversarial setup reproduced the original result and then some.

## Tests 4 and 5 — recombining and changing domains entirely

Two more direct tests of an obvious escape hatch: what if you combine two known ideas into one, or move to a completely different field? I combined the two puzzles from Test 3 into a single resolution — Apex matched it to "neutrino postulate plus relativity" at 95% confidence. I then pivoted entirely out of physics into biology, building a puzzle about a species evolving to help genetic relatives at a cost to itself — Apex matched it to Hamilton's kin-selection theory (1964) at 99%, and the disconfirmation-seeker again failed to hold a no-match position.

## A proposal I decided not to build

Someone I was discussing this with suggested an obvious next step: train a generator with reinforcement learning, and reward it every time it produces something Apex can't match to a known idea. I decided not to build this, for a specific reason rather than just running low on time: the moment "Apex can't find a match" becomes the reward signal, the fastest way to get reward isn't genuine novelty — it's obscurity. Vague phrasing, invented jargon nobody would search for, ideas deliberately built to dodge a search engine rather than ideas that are actually new. A generator optimized this way would converge on "incoherent but unsearchable," which is the opposite of what I wanted to measure. This is a specific, well-known failure mode (reward hacking) applied to this exact setup, not a vague worry — so I skipped it rather than build something I already expected to produce a misleading result.

## Test 6 — one more domain, then a full batch

A third domain pivot (a machine-learning phenomenon called double descent, where test error dips, rises, then falls again as model size increases) matched to the real published result at 95-98% confidence, disconfirmation-seeker included. Then I ran a full batch of four more, deliberately varied by the *type* of insight involved rather than just the topic: the discovery that hand-washing prevents childbed fever, a classic economics puzzle about information asymmetry in used-car markets, a WWII statistics story about survivorship bias in armor placement, and the general engineering principle of profiling before optimizing. All four matched at 95-99% confidence, no exceptions.

Running total across the whole Apex phase: **10 candidates tried, 10 matched, 0 stumped, across 7 different fields** (physics, biology, machine learning, medicine, economics, statistics, engineering).

## Checking against a formal theory of creativity, and looking for counterexamples

I checked this pattern against Margaret Boden's well-known framework for AI creativity, which distinguishes "combinatorial" and "exploratory" creativity (recombining or exploring within a space of ideas you already have) from "transformational" creativity (actually changing the space itself). Her own framework independently predicts something close to what I found: transformational creativity is recognizable only in hindsight, once a new space has been explored long enough to prove it's real — which means, almost by definition, you can't cleanly detect it in the moment with the tools available at the time.

I also looked for a real, documented case of an AI system unknowingly stumbling onto something genuinely good that later turned out to already exist — and found only near-misses, all explicitly built as rediscovery tests rather than genuine accidents. My honest read: this isn't because it doesn't happen, it's because normal scientific publishing already does the same prior-art check my toy Apex setup does, just at a much larger scale, before anything gets called "novel" and put into print — so an accidental, unnoticed rediscovery would very likely get caught at that stage and never surface as a clean documented case.

## Checking against real machine-learning theory

Separately, I checked three established results in ML theory that all turned out to independently point at the same underlying diagnosis:
- **Model collapse** — a well-documented, formally proven effect where training a model repeatedly on its own generated output narrows its distribution and loses information, with the only known fix being an injection of genuinely new outside data.
- **Weak-to-strong generalization** — a result showing a strong model can be usefully supervised by a weaker one, but (checked carefully, trying to argue against my own hypothesis rather than for it) this works by drawing out capability the strong model already has from richer training, not by creating something neither model possessed.
- **A formal result in generative adversarial network theory** — a mathematical proof that a generator trained against a same-data discriminator is bound to stay within the space it was trained on, with no known counterexample anywhere in the literature.

All three, independently, from three unrelated corners of ML theory, name the same missing ingredient: genuine access to information the system doesn't already have. Not a smarter algorithm. Not a bigger model. Outside access.

## Where this leaves it

I looked, seriously and adversarially, for a way to break my own conclusion, and I couldn't find one. If anything, the evidence for the conclusion got stronger than when I first reached it — 10 for 10, across 7 fields, with a purpose-built adversary failing every single time at the one job it had. I did leave one thread genuinely open rather than closing everything: a real but narrower question about whether a panel finds the *actual reason* something is false more often than a single judge, separate from just getting the right true/false answer. That thread sat unresolved for months until I finally went back and [tested it properly](../07-followup-test-2026/).
