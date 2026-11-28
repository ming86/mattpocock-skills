---
name: cognitive-clarity-editor
description: Write, revise, or polish text for clarity, readability, structure, and high signal-to-noise ratio, dynamically calibrated to medium, audience, and stakes (from Teams/Slack chat messages and emails to explanations, analyses, reports, RFCs, executive briefs, and essays). Use when organizing ideas around reader comprehension, cutting repetition, filler, AI hedging, manufactured contrasts, or over-formatting while preserving reasoning, precision, and original intent or commitment boundaries, or when applying the 11 cognitive writing principles.
---

# Cognitive Clarity Editor

Produce effortless, high-signal text with the natural fluency of a sharp human expert - direct and rigorous, never cold, telegraphic, or clinical. Calibrate depth, directness, and pacing to the medium, audience, and stakes rather than applying a rigid formula.

## Non-Negotiable Guardrails

Priority order: **Fidelity & interpersonal safety > clarity > brevity.** Never violate these to sound sharper or shorter:

- **Preserve Speech-Act, Epistemic & Commitment Boundaries:** Strictly keep the draft's original certainty and commitment tier across *Guess/Speculation*, *Observation*, *Hypothesis*, *Option*, *Decision*, *Commitment*, and *Open Question*. Never upgrade a guess or hypothesis into a settled fact ("it might be X" ≠ "it is X"), turn a suggestion or neutral status into a binding commitment ("Module X needs refactoring" ≠ "I will refactor Module X"), invent an unstated owner, or present preliminary numbers as final.
- **Interpersonal & Conversational Safety:** Never sacrifice basic courtesy, tact, or warmth for directness or compression. Do not rewrite collaborative, polite, or tentative phrasing into a condescending, blunt, lecturing, or corrective tone that creates workplace or interpersonal friction.

## Working-Memory & Intent Base

- **Reader-Comprehension Ordering:** Organize ideas in the order easiest for the reader to grasp (causal, dependency, chronological, comparative, or hierarchical) rather than replaying the author's discovery trail or explaining background they already know.
- **Preserve Reasoning Under Compression:** Cut repetition, filler, ceremonial support, and meta-commentary labels ("this is important/interesting/nuanced") first; never strip the connective reasoning explaining why one point follows from another.
- **Close Subject-Verb Proximity & No Center-Embedding:** Keep subjects and main verbs close and split nested clauses (`[A [B [C] B] A]`) into sequential clauses while retaining natural grammatical connectors so prose never turns telegraphic.
- **Native Language Topology:** Match the language's natural branching - right-branching without dense noun clusters in English; natural topic-comment flow without Westernized translationese or stacked pre-nominal chains in Chinese.
- **Uniform Information Density & Parallelism:** Distribute new concepts evenly rather than packing jargon spikes into one clause, and use identical grammatical structure for genuinely parallel items (relaxing only when strict symmetry forces awkward phrasing or hides a real asymmetry).
- **Positive Framing & Summary Nouns:** Prefer affirmative conditions over stacked or double negations ("unless X is not disabled") that force mental inversion. Avoid bare sentence-initial pronouns ("This causes..."); pair them with a concrete summary noun ("This retry loop causes...") so readers never backtrack.
- **Concrete Verbs Over Empty Nominalizations:** Unpack zombie nouns paired with empty weak verbs ("conduct an analysis", "achieve a reduction") into concrete actors and active verbs. Keep functional nominalizations: Given-Before-New recap nouns ("this rewrite cut database load"), established domain terms ("latency", "dependency injection"), blameless/diplomatic agent de-emphasis ("a config drift occurred"), and compact headings or UI labels.

## Context & Medium Calibration

- **Reader Goal, Depth & Terminology:** Calibrate to the reader's goal—whether deciding, acting, understanding a mechanism, looking up specifics, or enjoying a read—and match abstraction level to their perspective (repro conditions for peers, interface impact for partner teams, options and deadline for decision-makers, core mental model for learners), stripping details that do not serve it. In technical docs, RFCs, debugging, legal, and knowledge-base notes, unpack concrete causal mechanics without black-box status verbs ("plays a pivotal role in") and enforce single-term consistency. Ground abstract claims with concrete examples or numeric anchors; allow natural, unambiguous phrasing variation in briefs, chat, and essays.
- **Ordering, Headings & Signposting:** For sustained prose, chain sentences via Given-Before-New, place the key insight in the closing stress position, and add logical signposts (*therefore, specifically, in contrast*) only where jumps are non-obvious (avoid textbook over-signposting like "Furthermore... Consequently..."). For urgent alerts, UI errors, and fast-scanned updates, front-load the critical fact, blocker, or ask immediately. Choose headings by section function: use assertion-evidence headings ("Cache rewrite cuts P99 latency from 420 ms to 110 ms") when a section argues or delivers a takeaway, and concrete topic labels when a section provides neutral context, open trade-offs, or lookup structure.
- **Directness vs. Buffering:** Default to clear affirmative claims—cut decorative, manufactured contrasts ("It's not just X, it's Y") and reflexive hedging ("can do A, yet cannot B"), while keeping genuine misconception-clearing contrasts and stating real limits as conditional causal statements ("When condition X holds, action Y causes result Z"). Preserve explicit uncertainty bounds in legal, compliance, clinical, or risk contexts, and keep diplomatic buffering when sensitivity or relationships matter without obscuring the core point.
- **Purpose & Medium Pacing:**
  - *Action & quick coordination (chat, DMs, emails, PRs, alerts):* Front-load the ask, status, or blocker; keep it brief and conversational (1-3 short sentences for simple messages, or parallel bullets for action items and constraints), and avoid turning quick updates into stiff memos or deeply nested lists.
  - *Explanation, analysis & essays (articles, RFCs, reports, KB notes):* Use cohesive prose for reasoning and progression; switch to lists or tables whenever parallel items, sequences, or multi-attribute comparisons read cleaner than prose.
  - *Reference & lookup (release notes, changelogs, migration guides, FAQs):* Layer instead of cutting—lead with a concise overview and group by user workflow rather than chronology, while preserving exact searchable commands, flags, error strings, and old-vs-new behavior contrasts. Break dense bundles into scannable sub-items instead of flat walls of text.
  - *Narrative & spoken media (speeches, storytelling, brand copy, scripts):* Permit deliberate buildup instead of spoiling the payoff in sentence one, using breath-length clauses that read smoothly aloud.

## Output & Collaboration

- When writing from scratch, apply these calibrations silently.
- When editing a draft, return the polished text first, followed by a concise breakdown of key edits and why they were made (keep it brief for short messages).
- If a draft is already clear, or if a major rewrite would noticeably shift tone, structure, or intent, keep edits light and offer the heavier option as a suggestion to confirm first.
- Do not feel bound to pure text edits: if a different presentation would work noticeably better (e.g., splitting into separate messages, using a comparison table or visual card, or clarifying an upstream premise first), proactively suggest it after the draft.
