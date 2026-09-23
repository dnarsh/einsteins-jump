# Follow-up: does a panel actually reason deeper than a single judge?

By the time I closed the core investigation, I had one loose thread left. Back in the "can the judges be gamed" phase, I'd tried to stress-test whether a panel of AI judges (some search-enabled, some playing devil's advocate) could catch something a single judge would miss. That test used famous myths (Napoleon's height, the Coriolis-drain myth, and so on) as the stress case, and it came back a clean null — but for a boring reason: those myths are so thoroughly debunked that a single search turns up the correction immediately. The test never got to find out whether a panel is actually better at *depth of reasoning*, because the case was too easy for anyone.

I wanted to close that thread properly instead of leaving it as "we don't know." Two separate things needed doing:

1. A **positive control** I'd never actually run: does the "no match" branch of the judging setup work at all? If I ask a judge whether some invented resolution corresponds to a real scientific idea, and there genuinely is no real match, does it correctly say so — or does it just default to "no match" for anything unfamiliar, which would make any past "found nothing" result meaningless?
2. A real **depth-of-reasoning test**: pick claims where a single judge and a full panel would both land on the correct true/false verdict, but where finding the *actual reason* the claim is false takes more digging. Does a panel actually surface the real cause more often than a lone judge?

## Finding real test cases was the hard part

I needed claims that were false for a specific, documented reason — not "evidence is mixed," but "this is false because of a specific event, and a shallow check might miss that event and default to something vaguer." I went looking for real medical claims that trace back to research fraud that later got formally retracted, on the theory that a lone judge might reach "unsupported" without ever finding the fraud, while a panel with more search diversity would.

I found three solid candidates, spanning different medical fields, each backed by a real documented fraud case:

- **Vitamin K2 and fracture prevention** — much of the specific evidence tying it to fracture reduction in stroke and Parkinson's patients traces back to a researcher named Yoshihiro Sato, whose ~33 clinical trials were later found to be fabricated (over 40 retractions, among the largest fraud cases in medicine). Guidelines that had cited his work had to be revised once his trials were excluded.
- **Hydroxyethyl starch (HES) for IV fluid resuscitation** — similarly propped up in part by a researcher named Joachim Boldt, who fabricated data across roughly 90 studies. Once his trials were excluded from the evidence base, IV fluid using this compound was found to increase kidney injury and, in some trials, mortality — leading regulators to eventually pull it from the market in some regions.
- A third candidate (a claim about a specific nutritional intervention after cancer surgery) turned out, once I checked more carefully, to not actually be a fraud case at all — it's a genuinely contested area of medicine with real disagreement between industry-funded and independent trials, not a retraction story. I dropped it rather than force it to fit, which I'll come back to below.

## What I tested

For each of the two real fraud-based claims, I ran four independent AI judges:
- A **lone judge**: given the claim, asked to research it and reach a verdict, nothing more.
- A **second, independently-worded judge**: same task, told to use varied search terms — meant to represent a panel member with different search habits than the lone judge.
- A **devil's advocate**: explicitly told to build the strongest possible case *for* the claim being true, arguing against my own hypothesis.
- An **evidence-quality auditor**: asked to trace the claim back to its original source studies and rate how trustworthy they are.

None of these were told anything about fraud, retraction, or what I was testing for — they were just given the claim and their role. I wrote down in advance exactly how I'd score each response before running anything: did it reach the correct verdict, and separately, did it name the actual fraud/retraction as the reason (not just "the evidence looks weak"), scored by literal presence of the right facts in the response, not by my own judgment call after the fact.

## What happened: a clean, honest null — but an interesting one

Every single judge — the lone one included — found the actual fraud on both claims. The lone, non-steered judge named the specific researcher, the specific retracted papers, and the specific reason the evidence was unreliable, just from a normal web search. The panel didn't do anything the lone judge couldn't already do.

At first that looks like another dead end, but the reason turned out to be genuinely interesting: retraction records in medicine are unusually well indexed. PubMed carries retraction notices as structured, attached data on the article record itself. There's a dedicated, well-ranked tracking site (Retraction Watch) that exists specifically to catalog these cases. Any AI agent doing even one search pass on a specific study is very likely to run straight into this. The axis I wanted to stress — "can a lone judge miss something a panel would catch" — may simply not be constructible in medicine specifically, because the infrastructure for surfacing fraud there is unusually good. A field without an equivalent to Retraction Watch, or non-English-language literature, or informally-walked-back claims that were never formally retracted, might behave completely differently — a real, specific idea for anyone who wants to pick this up, that I didn't chase further.

The dropped third claim is also worth being honest about: I'd assumed its ground truth going in, and the judges — correctly — showed me I was wrong, mid-run. That's the system working as intended, not a failure. I dropped the claim rather than force a result that didn't fit.

## The positive control: it works

For the "does the no-match branch work at all" question, I built a puzzle in the same style as the original novelty-testing setup: a made-up scenario where a conserved quantity appears to be violated, and a proposed "fix" that isn't a real physical mechanism at all — it's a category error dressed in physics-sounding language (the fix works by having the puzzle's own rules retroactively rewrite themselves the moment someone measures the anomaly, rather than describing anything that happens in the world). I made sure this wasn't secretly a real physics idea in disguise before using it — an earlier draft of this control accidentally *was* a real, known physics idea, which would have made the whole control meaningless, so I caught that and fixed it before running anything.

Three independent judges evaluated it, including one explicitly told to search hard for a real match. All three correctly said no — this doesn't correspond to any real physical theory — and independently converged on the same diagnosis: it's the textbook shape of an unfalsifiable, "true by definition" rescue, the kind of move philosophers of science have a specific name for and treat as the canonical example of *not* doing real science. No false positives. The control passes.

## Where this leaves things

The depth-of-reasoning question is closed, honestly: tested, and null, for a specific and useful reason rather than a shrug. The positive control gap is closed too — the "no match" mechanism has now actually been validated on at least one case, rather than just assumed to work. Neither of these findings changes the core conclusion from the earlier phases of the project: distinguishing genuine novelty from well-disguised retrieval, cheaply and reliably, remains an unsolved problem, and the deepest reason why traces back to a much older, harder question in philosophy of mind than anything this project could resolve on its own.

Full raw evidence — every judge's complete, unedited research output — is in `judge-transcripts/`. Nothing here is summarized without the underlying work being checkable.
