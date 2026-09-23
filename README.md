# Einstein's Jump

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Phases](https://img.shields.io/badge/phases-7-informational)
![Status](https://img.shields.io/badge/status-closed%2C%20honest%20negative%20result-lightgrey)

**Can you build a test that tells you whether an AI actually invented something new — as opposed to cleverly recombining something it already knew?**

I spent about a month on this as a side project. Short answer: no, not cheaply, not with anything I could build solo — and the reason why turns out to be a genuinely interesting, 50-year-old open problem in philosophy of mind, not just an engineering gap. This repo is the honest record of that attempt: what I tried, what broke, what I learned, and why I eventually closed it rather than kept pushing.

## The question

Ask an AI to solve a hard problem, and it gives you a great-sounding answer. How do you tell whether it just found a genuinely new insight, or whether it recognized the problem as a disguised version of something already in its training data and served up a repackaged answer? This matters a lot if you ever want to trust an AI to do real scientific or mathematical discovery — "sounds novel" and "is novel" are not the same thing, and conflating them is an easy way to fool yourself.

The name is a reference to the kind of leap I was hoping to measure: not incremental improvement, but the moment where a real insight clicks — the way Einstein didn't just extend Newtonian mechanics, he saw that the whole frame was wrong.

**If you only have five minutes:** read [phase 1](01-first-attempt/) for the first wall I hit, [phase 6](06-building-apex/) for the part where I tried hardest to prove myself wrong and couldn't, and [phase 5](05-why-this-is-hard/) for the actual reason, which turned out to be more interesting than the negative result itself.

| Phase | Question | Outcome |
|---|---|---|
| [1. First attempt](01-first-attempt/) | Can a disguised physics puzzle fool an AI judge into calling it novel? | No — 6/6, caught instantly. Structural, not fixable by better disguise. |
| [2. Second attempt](02-second-attempt/) | Does generation outperform verification on a different kind of riddle? | Inconclusive — never found an item difficulty where the test had room to run. |
| [3. Competence check](03-competence-check/) | Can I replicate a real published result correctly, end to end? | Yes — 5/5 seeds, clean, honestly compared against the source paper. |
| [4. Can the judges be gamed?](04-can-the-judges-be-gamed/) | Can a panel of judges be fooled by shared blind spots or framing? | Mixed — independence fixes independent errors, not shared ones; framing softens confidence but never flips a verdict. |
| [5. Why this is hard](05-why-this-is-hard/) | Has *anyone*, in any field, solved this? | No — 13 independent fields, same wall, traced to a 50-year-old open problem in philosophy of mind. |
| [6. Building Apex](06-building-apex/) | Can I break my own conclusion with the most adversarial test I can build? | No — 10/10 matched, 0 stumped, across 7 fields. The conclusion held up harder than when I started. |
| [7. Follow-up, months later](07-followup-test-2026/) | Does a panel find the *real reason* a claim is false more often than one judge? | No — but for a specific, interesting reason, plus a validated control I'd never run. |

## What I actually tried, in order

**1. [First attempt](01-first-attempt/) — a synthetic puzzle in made-up vocabulary.**
Build a physics-shaped puzzle using entirely invented terms, so an AI can't just pattern-match against a real physics fact it memorized. Two independently-designed "solutions" to the puzzle both got instantly recognized by AI judges as disguised versions of real physics (the neutrino postulate; special relativity) — 6 out of 6, every time. Turns out any puzzle shaped like "a conservation law appears violated" funnels toward the same handful of famous real answers, no matter how you disguise the vocabulary. Not a bug I could fix — a structural property of that kind of puzzle.

**2. [Second attempt](02-second-attempt/) — a harder-to-fool version of the puzzle.**
The first attempt's puzzle turned out to be too generous a target — its shape alone was a giveaway. Second attempt flipped it around: a different kind of riddle entirely, and a design that separates an AI's ability to *generate* an answer from its ability to *verify* one, since those two skills can decouple in interesting ways. A properly calibrated pilot ceilinged out — no room left to work with once the difficulty was tuned correctly — closing this specific design honestly rather than overclaiming a partial result.

**3. [A competence check, unrelated to the main question](03-competence-check/) — replicating a real, published result.**
Before trusting my own methodology on the harder question, I wanted proof I could execute a rigorous experiment correctly end-to-end, on real compute, against a real published result. I replicated "grokking" — a known effect where a small neural network trained on simple arithmetic suddenly jumps from memorizing to actually generalizing partway through training. Includes the actual code. 5 out of 5 runs grokked cleanly, which is a stronger and more consistent result than the paper I was replicating found — explained honestly in the writeup, not oversold.

**4. [Can the judges themselves be gamed?](04-can-the-judges-be-gamed/) — five small toy experiments.**
A side-question that turned out to matter a lot: once you're using a panel of AI judges to catch mistakes, can that panel itself be systematically fooled? Five small toys probing different angles of this, with one finding that held up twice: independence between judges fixes errors that are independent of each other, but if all your judges share the same blind spot, adding more of them doesn't help — you have to break the shared constraint directly.

**5. [Why this is actually hard](05-why-this-is-hard/) — the real answer.**
After hitting walls twice, I went looking for the deeper reason, across a genuinely wide literature search — AI evaluation, AI-for-science, computational creativity, mechanism design, philosophy of science, patent law, developmental psychology, and more. The pattern: nobody, anywhere, has a working way to certify "this is both novel and correct" without either (a) already having an answer key to check against — which just proves the idea was a known type of thing — or (b) moving that answer key somewhere else you can't fully audit (a corpus, a judge's own prior knowledge, a later real-world experiment). This connects directly to a real, still-unresolved problem in philosophy of mind from 1975 (Fodor's paradox of concept acquisition): you arguably can't learn a genuinely new primitive concept through hypothesis-testing, because forming the hypothesis already requires the concept you're trying to learn. That's not a metaphor — it's a serious, structural argument, and nobody has a clean rebuttal to it 50 years later.

**6. [Building Apex, and trying my hardest to break my own conclusion](06-building-apex/) — eight adversarial tests in a row.**
Reaching a strong conclusion is exactly when it's easiest to talk yourself into stopping too early. So I built the most adversarial detector I could — a panel of AI judges with a dedicated devil's-advocate role whose entire job was to argue against whatever the honest answer looked like — and threw everything at it: famous myths (null, too easy), a properly graduated difficulty ladder including a real medical-fraud case (still null, but surfaced a real loose thread about depth of reasoning), my own earlier puzzles run through a harder mechanism (reproduced, even more convincingly), combined and cross-domain versions (matched every time), a reinforcement-learning idea I deliberately declined to build (and explained exactly why), and a final batch bringing the running total to 10 out of 10 matched, 0 stumped, across 7 completely different fields. I couldn't break my own conclusion. If anything, it came out stronger than when I started.

**7. [A follow-up test, months later](07-followup-test-2026/) — closing the one thread I'd left open.**
I came back to this after it had been closed for a while, to test the one thing I'd never actually checked: does a panel of judges find the *real reason* a claim is false more often than a single judge does, on cases where both reach the same correct true/false verdict? Built real medical test cases around documented research-fraud scandals, pre-registered exactly how I'd score it before running anything, and got a clean, honest null again — but for a genuinely interesting reason this time (medical retraction records are unusually well-indexed, so a single search reliably finds them). Also ran a control I'd never gotten around to: does the "no match" branch of the judging setup work at all, or does it just default to "no match" for anything unfamiliar? It works — validated on a real test case for the first time.

## What this actually shows

I'm not going to pretend this project discovered anything new about how to detect AI novelty — it didn't, and the honest conclusion is that nobody currently has a cheap way to do it. What I think this repo actually demonstrates:

- **Pre-registering a test before running it, every time** — writing down what counts as success or failure before you see the result, so you can't quietly move the goalposts afterward.
- **Treating a clean negative result as a real result**, not a failure to hide. Several of the most interesting findings here are "this doesn't work, and here's precisely why" — which is more useful than a vague "it's complicated."
- **Catching my own mistakes before they became false claims** — an early version of the final control in the 2026 follow-up was accidentally a real physics idea in disguise, which would have made the whole test meaningless. I caught it before running anything, not after.
- **Actually closing threads instead of leaving them open forever.** The 2026 follow-up exists because I had one genuinely untested idea left over from months earlier, and I went back and tested it properly instead of letting it sit as an unresolved "maybe."

## Layout

Each numbered folder is a phase, in chronological order, with its own README telling that phase's story plus the underlying pre-registrations, results, and (where applicable) raw code or raw judge transcripts, so nothing here is a bare claim — the underlying evidence is checkable.
