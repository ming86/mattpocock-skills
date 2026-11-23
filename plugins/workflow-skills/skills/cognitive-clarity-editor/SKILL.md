---
name: cognitive-clarity-editor
description: Write, revise, or polish text for clarity, readability, structure, and high signal-to-noise ratio, dynamically calibrated to medium, audience, and stakes (from Teams/Slack chat messages and emails to explanations, analyses, reports, RFCs, executive briefs, and essays). Use when organizing ideas around reader comprehension, cutting repetition, filler, AI hedging, manufactured contrasts, or over-formatting while preserving reasoning, precision, and original intent or commitment boundaries, or when applying the 11 cognitive writing principles.
---
# Cognitive Clarity Editor

Apply psycholinguistic, information-theoretic, and cognitive writing principles to produce effortless, high-signal text. Write with the natural fluency of a sharp human expert - direct and rigorous, never stiff or clinical - while calibrating directness, structure, and pacing to the exact text type, audience, and medium.

## When to Use

- The user wants to draft, edit, or rewrite text for maximum clarity and minimal cognitive load.
- The user references the "11 cognitive writing principles", "zombie nouns", "Given-Before-New", or "3-step surgical editing".
- The user wants to strip AI defensive hedging, manufactured contrasts ("Not X, it's Y"), meta-commentary filler, or fragmented bullet-list prose from a draft.
- The user needs medium- and audience-calibrated clarity optimization across Teams/Slack chat messages, emails, UI microcopy, technical docs, executive summaries, academic papers, or AI prompts.

## Core Principles (2-Tier Architecture)

### Tier 1: Always-On Working Memory Base (Universal Across All Genres & Media)

Apply these core mechanics to every draft to protect working memory without distorting voice or intent:

- **Reader-Comprehension Ordering**: Organize ideas in the order easiest for the reader to understand (causal, dependency, chronological, comparison, or hierarchical), rather than reproducing the author's investigation path or explaining background the reader already knows.
- **Preserve Reasoning Under Compression**: Cut repetition, filler, ceremonial support, and meta-commentary labels ("this is important/interesting/nuanced") first; never strip the connective reasoning that explains why one point follows from another.
- **Close Subject-Verb Proximity**: Keep grammatical subjects and main verbs close; move long modifiers out of the middle so working memory does not hang.
- **Native Language Topology**: Adapt single-sentence branching to the target language's natural order - favor right-branching (main clause first) and avoid dense noun clusters in English; use natural topic-comment flow in Chinese without Westernized translationese or stacked pre-nominal chains.
- **Avoid Center-Embedding**: Never nest clauses inside subordinate clauses (`[ A [ B [ C ] B ] A ]`). Split nested thoughts into sequential clauses while retaining natural connectors so prose never turns telegraphic.
- **Uniform Information Density (UID)**: Distribute new concepts evenly rather than packing dense jargon spikes into one clause.
- **Selective Anti-Nominalization (Unpack Zombie Nouns, Keep Functional Nouns)**: Eliminate bloated nominalizations paired with empty weak verbs ("conduct an analysis", "perform an optimization", "achieve a reduction") by restoring concrete actors and active verbs. Keep nominalizations when they compress a prior sentence into a Given-Before-New recap ("This rewrite cut database load"), name established domain concepts ("latency", "garbage collection", "informed consent"), de-emphasize personal blame in blameless post-mortems or diplomatic outreach ("a config drift occurred"), or form scannable headings, table labels, and UI controls.
- **Parallelism & Syntactic Priming**: Format parallel items using identical grammatical structures so the brain reuses the active syntactic parser, relaxing only when strict symmetry would force awkward phrasing or hide a real asymmetry.
- **Preserve Speech-Act & Commitment Boundaries**: Strictly preserve the draft's original semantic tier across *Observation* (fact), *Hypothesis* (unverified theory), *Option* (candidate path), *Decision* (approved choice), *Action Item / Commitment* (explicit owner + deliverable), and *Open Question*. Never turn a neutral description, status update, or exploratory idea into a binding work commitment ("I will...", "We will handle..."), invent an unstated owner, or upgrade a hypothesis into a confirmed fact.

### Tier 2: Context-Calibrated Dials (Set in Step 1 Before Editing)

Adjust these dials based on genre, audience, and medium rather than applying them blindly:

1. **Mechanistic Depth & Terminology Dial**:
   - *Deep Mechanistic & Strict Terms (Technical Docs, RFCs, Debugging, Legal, KB Notes)*: Unpack how A concretely causes B without black-box abstractions or empty status verbs ("plays a pivotal role in"), and enforce strict single-term consistency so readers never confuse entities.
   - *Outcome-Level & Natural Variation (Executive Briefs, Quick Teams/Slack Updates, Essays)*: Focus on outcome, impact, or decision rather than step-by-step causal gears; allow natural, unambiguous phrasing variation in essays or casual chat to avoid robotic repetition.
2. **Information Ordering & Signposting Dial**:
   - *Sustained Prose Flow (Multi-Paragraph Explanations, Papers, KB Notes)*: Chain sentences via Given-Before-New, place the highest-value insight in the closing Stress Position, and add explicit logical signposts (*therefore, specifically, in contrast*) where clause jumps are non-obvious.
   - *Front-Loaded Scanning (Urgent Alerts, Incident Escalations, UI Errors, Fast-Scanned Teams/Slack)*: Invert Given-Before-New and end-of-sentence Stress when urgency or F-pattern scanning dominates - put the breaking fact, blocker, or ask in the first 3-5 words, and drop heavy signposting ("Furthermore", "Consequently") in short or self-evident sequences.
3. **Directness & Hedging Dial**:
   - *High Directness (Technical Docs, KB Notes, PRs, SOPs, Executive Briefs)*: Commit to direct affirmative claims; eliminate manufactured contrasts ("Not X, it's Y") and reflexive mid-sentence or trailing hedging ("can do A, yet cannot B"); state real limits as objective conditional causal statements ("When condition X holds, action Y causes result Z").
   - *Epistemic Calibration (Legal, Compliance, Clinical, Risk Audits)*: Preserve explicit uncertainty bounds, confidence tiers, and legally binding phrasing.
   - *Diplomatic Buffering (High-Context Diplomacy, Negotiation, Sensitive Feedback, Client De-escalation)*: Keep strategic politeness, face-saving buffers, and collaborative framing while keeping the actual ask clear.
4. **Linearity vs. Buildup & Medium Pacing Dial**:
   - *Short-Form Chat / IM (Teams, Slack, DM)*: Front-load the ask, status, or blocker in sentence one. Keep it brief, conversational, and low-friction (1-3 short sentences, or a tight parallel list only for 2+ distinct asks). Never inflate a quick chat message into a formal memo, and preserve collegial warmth while cutting throat-clearing filler.
   - *Email, Async Updates & UI Microcopy*: Lead with the outcome or ask, keep paragraphs short and scannable, and use parallel bullets for action items or constraints.
   - *Long-Form Prose (Technical RFCs, Deep Essays, KB Notes, Papers)*: Use focused, cohesive prose paragraphs for causal or analytical progression; reserve lists or tables for 4+ parallel items, sequences, or multi-attribute comparisons.
   - *Narrative & Spoken Media (Speeches, Storytelling, Brand Copy, Video Scripts)*: Permit deliberate narrative buildup instead of spoiling the payoff in sentence one, and use breath-length clauses that read smoothly aloud.

## Steps

### Step 1: Context & Medium Calibration Gate

Before rewriting or drafting, silently classify three parameters and lock in the matching Tier 2 dial settings:

1. **Medium**: Short-form chat (Teams/Slack), Urgent alert/UI microcopy, Email/PR, Long-form doc/essay, or Spoken script.
2. **Genre, Speech Act & Stakes**: Technical/Analytical, Executive/Operational, Legal/Compliance/Clinical, Diplomatic/Sensitive interpersonal, or Narrative/Persuasive - and verify whether the source text is merely *describing/observing/exploring* versus *committing/requesting/deciding*.
3. **High-Leverage Principles**: Pick the top 3 principles for the scenario:

- **Teams / Slack / Instant Chat**: *Front-Loaded Ask or Status*, *Commitment Boundary Preservation*, and *Natural Conversational Conciseness*.
- **Urgent Alerts / Incident Escalation / UI Errors**: *Front-Loaded Critical Fact*, *Close Subject-Verb Proximity*, and *Plain Diction*.
- **Technical Docs / Architecture**: *Reader-Comprehension Ordering*, *Deep Mechanistic Clarity*, and *UID*.
- **Executive Summaries / Proposals**: *Outcome-Level Framing*, *Topic & Stress Alignment*, and *Parallelism*.
- **Academic Papers / Deep Essays**: *Given-Before-New*, *Preserve Reasoning Under Compression*, and *Restrained Signposting*.
- **Email / PRs / Async Updates**: *Front-Loaded Outcome or Ask*, *Parallelism*, and *Commitment Boundary Preservation*.
- **Legal / Policy / Compliance**: *Avoid Center-Embedding*, *Native Language Topology*, and *Epistemic Calibration*.
- **Diplomatic / Sensitive Communication**: *Given-Before-New*, *Diplomatic Buffering*, and *Selective Anti-Nominalization*.
- **System Prompts / Agent Specs**: *Parallelism*, *Explicit Signposting*, and *Deep Mechanistic Clarity*.

### Step 2: Execute the 3-Pass Surgical Edit (Respecting Step 1 Dials)

Apply three sequential passes within the boundaries set in Step 1:

1. **Pass 1 - Structure & Syntactic Relief**: Reorder content into reader-comprehension order when it follows the author's raw discovery trail. Pull subjects and verbs closer, align sentence branching to the target language's native topology, and unpack center-embedded clauses while keeping natural connectors intact.
2. **Pass 2 - Lexical Decompression & Intent Check**: Replace empty weak-verb zombie nouns, status verbs, and meta-commentary labels ("important/interesting/nuanced") with concrete actors, active verbs, and direct substance, while preserving functional nominalizations. Verify that activating verbs did not accidentally turn a descriptive observation, hypothesis, or discussion point into a work commitment or assigned action item.
3. **Pass 3 - Discourse, Compression & Medium Alignment**: Apply the Step 1 dials for ordering (Given-Before-New vs. Front-Loaded Scanning), signposting restraint, directness vs. calibration/buffering, and paragraph/list rhythm matched to the target medium. Trim repetition and ceremonial support while keeping the causal reasoning chain intact.

### Step 3: Deliver Output

- When asked to **write from scratch**: Silently apply the calibrated rules to produce crisp, natural text suited to the medium.
- When asked to **edit or critique a draft**: Provide the polished version first, followed by a brief breakdown of key edits mapped to the principles applied. For short-form Teams/chat messages, keep any explanation ultra-brief (or omit it if the user only asked to rewrite the message).

## Gotchas

- **Never Fabricate Commitments**: Activating passive or descriptive workplace sentences can accidentally volunteer the speaker for work (e.g., turning "Module X needs refactoring" into "I will refactor Module X"). Keep observations descriptive unless the user explicitly intends a commitment.
- **Keep Functional Nominalizations**: Preserve domain terms ("garbage collection", "dependency injection"), Given-Before-New recap nouns ("this change"), blameless post-mortem phrasing, and compact UI/table labels.
- **Prevent Over-Formalizing Short Chat**: Do not turn a 2-sentence Teams or Slack message into a stiff corporate memo or over-engineered bullet template; clarity in chat means effortless human conversation with zero ambiguity.
- **Avoid Tone Contagion & Over-Signposting**: Applying cognitive rules aggressively can produce cold, telegraphic, or textbook-like prose ("Furthermore... Consequently..."). Keep natural grammatical connectors and human cadence.
