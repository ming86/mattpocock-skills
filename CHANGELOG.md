# Changelog

## 0.2.17 - 2026-08-31

- Preserve scope status across workflow transformations: requirements and current decisions remain part of the current work, while assumptions, unresolved points, and agent-proposed additions remain labeled as such instead of being promoted into durable requirements.
- Make `to-spec` carry forward existing validation requirements without inventing new supporting work, and make `to-tickets` decompose the source work without silently creating preparatory refactors, prerequisites, validation commitments, or other tickets.
- Align `implement`, Wayfinder, `workflow-guide`, repository maintenance guidance, and package documentation so newly discovered scope-expanding work is surfaced as a proposal while ordinary focused checks and already-required project work continue normally.

## 0.2.16 - 2026-08-31

- Reduce repeated lists of optional supporting checks in `to-spec`, `to-tickets`, and `implement` so the skills keep supporting work scoped without repeatedly making gates, preflights, benchmarks, rollout, rollback, or similar machinery salient.
- Restore prototype-result semantics in specs and tickets: carry forward what an experiment showed and how it informed the current conclusion or decision rather than describing the prototype as having chosen the direction.
- Remove the remaining validation aside from the headline `codebase-design` principles so useful boundaries are justified by software structure and concrete dependency-control needs rather than test or validation salience.

## 0.2.15 - 2026-08-31

- Treat plans, specs, findings, assumptions, and decisions as current engineering state that can evolve as implementation or investigation reveals more, rather than describing ordinary work with unnecessary proof or finality language.
- Use direct descriptions of what is observed, chosen, changed, or still uncertain across debugging, domain modeling, clarification, specs, tickets, implementation, review, prototypes, research, handoff, and Wayfinder while keeping investigative evidence and genuine technical invariants where they carry useful meaning.
- Align repository maintenance guidance and package documentation with the same iterative model of engineering work without weakening the workflow-scope and validation boundaries introduced in 0.2.14.

## 0.2.14 - 2026-08-31

- Make workflow support scale to the actual work so specs, tickets, workflow transitions, and artifact sections do not manufacture new validation, review, benchmarking, preflight, rollout, rollback, or other supporting obligations.
- Recenter `codebase-design`, `to-spec`, `to-tickets`, and `implement` on the requested outcome: testability supports useful design rather than driving it, validation is conditional and outcome-derived, ticket boundaries do not become validation boundaries, and implementation uses the smallest representative checks the work actually needs.
- Narrow TDD routing to work where test-first development is explicitly requested or established by project instructions, and refine debugging, implementation review, merge-conflict resolution, handoff, workflow routing, repository maintenance guidance, and package documentation to avoid cross-skill assurance amplification.

## 0.2.13 - 2026-08-28

- Reframe `grilling` around uncertainty that can change or unblock useful work, choosing the right source for each question instead of assuming the model can pre-classify facts or user-owned decisions.
- Ground `grill-with-docs`, `research`, `prototype`, `to-spec`, Wayfinder, and questionnaires in the distinction between what project sources show, what is inferred, what remains assumed, and where user or expert input is actually needed.
- Prefer positive methodological guidance in repository maintenance instructions, reserving strong prohibitions for hard boundaries and recurring failure modes, and add routing cases for ordinary implementation judgment and external expertise.

## 0.2.12 - 2026-08-25

- Repair scope and routing distinctions that were weakened during the 0.2.11 prose cleanup while keeping the more natural engineering language.
- Restore the well-scoped implementation boundary, consequence-based unresolved-decision handling in specs, the explicit distinction among requirements, project facts, assumptions, and unresolved points, and direct-source reasoning for merge conflicts.
- Tighten `workflow-guide` triggers for implementation, implementation review, and external-owner questionnaires, and keep handoffs focused on unresolved state the next context actually needs.

## 0.2.11 - 2026-08-25

- Use more direct engineering language in selected workflow guidance where formal abstractions obscured concrete actions, while keeping specialized terms where they carry real technical meaning.
- Refine `workflow-guide` routing prose around concrete situations and consequences while preserving the prospective triggers introduced in 0.2.9.
- Simplify `to-spec`, `implement`, merge-conflict, handoff, and Wayfinder wording without changing their workflow responsibilities, stopping conditions, or routing boundaries.

## 0.2.10 - 2026-08-25

- Rewrite governance-heavy workflow wording into direct engineering language while preserving the same stopping, scope, evidence, and user-decision boundaries.
- Replace abstract `authority`/`authoritative` phrasing in debugging, implementation review, specs, Wayfinder, handoff, questionnaires, and domain modeling with concrete descriptions of the requested work and current project state.
- Prefer `current` or `agreed` plans over approval-oriented wording where no actual permission boundary is involved, and align repository-maintenance guidance with the same plain-language style.

## 0.2.9 - 2026-08-25

- Strengthen `workflow-guide` from a current-state catalog into a prospective router that recognizes explicit workflows that are relevant now or becoming relevant and surfaces them at useful transition points.
- Restore material trigger and timing nuance from the explicit workflow descriptions so the guide can suggest clarification, specs, ticket decomposition, review, handoff, and other workflows before their need becomes obvious.
- Extend routing cases for prospective suggestions of `grill-with-docs`, `to-spec`, `to-tickets`, `implementation-review`, and `handoff`, and align Workflow Guide harness metadata with the same semantics.

## 0.2.8 - 2026-08-25

- Generalize `codebase-design` dependency guidance from a fixed local/remote/vendor taxonomy to overlapping dependency characteristics and common shapes that also fit systems, native, device, tooling, and service software.
- Use broader domain terminology where the guidance is not specifically about business software, and diversify a small number of TDD examples beyond web/SaaS application patterns.
- Remove the unnecessary `most repos` topology claim from the domain-modeling context template.
- Synchronize all plugin and marketplace manifests at version `0.2.8`.

## 0.2.7 - 2026-08-25

- Compose `grill-with-docs` directly with `grilling` and `domain-modeling` through the Skill tool instead of partially restating those skills' procedures.
- Make implementation review resolve intent from the current authority and chronology of requirements and decisions rather than implying a fixed precedence among specs, plans, and the current request.
- Rename `to-tickets` output from `Acceptance criteria` to `Completion criteria` and define it as observable conditions or evidence that establish the intended outcome.

## 0.2.6 - 2026-08-23

- Reconcile the previous orchestration cleanup around a stable boundary: skills describe how to perform and interpret their workflow, while project-level instructions govern surrounding orchestration and authorization.
- Keep useful removals of worker topology, reviewer spawning, commit policy, checkpoint boilerplate, and other project-level mechanics from skill procedures.
- Replace vague `surface it` wording and defensive `does not authorize/replace/satisfy` disclaimers with workflow-specific semantics: what an artifact establishes, what remains unresolved, and where the procedure itself stops.
- Clarify prototype, implementation review, merge-conflict, handoff, questionnaire, design-comparison, and durable-state boundaries without turning those skills into policy wrappers.

## 0.2.5 - 2026-08-23

- Refine the orchestration-residue cleanup so skills may still reinforce authority and handoff boundaries that are intrinsic to the procedure.
- Clarify that focused implementation review does not satisfy broader review required by project instructions, implementation completion does not bypass required review or user checkpoints, prototype evidence does not authorize dependent implementation, and drafting a questionnaire does not authorize sending it.
- Keep worker topology, delegation, fresh-context, parallelism, reviewer-spawning, and generic orchestration boilerplate out of skill procedures.
- Restore project-convention context where it directly affects prototype artifact handling, and make material ambiguity/tradeoff wording surface decisions without prescribing how the Root orchestrates them.

## 0.2.4 - 2026-08-23

- Remove leftover orchestration boilerplate from skill bodies and references, including background-agent, worker-topology, reviewer-spawning, parallelism, checkpoint, and commit-policy commentary.
- Keep boundaries that are intrinsic to the procedure, but express them directly instead of routing them through generic governing-policy language.
- Keep material artifact-authority and decision-status boundaries while leaving delegation, review topology, user checkpoints, and follow-on workflow choices to project-level instructions.

## 0.2.3 - 2026-08-23

- Keep `grilling` from turning model-generated hypothetical edge cases into user-owned decisions.
- Require clarification questions to be grounded in the user's stated goal, project evidence, established constraints, or a concrete ambiguity in the requested work.

## 0.2.2 - 2026-08-23

- Simplify `workflow-guide` into a compact catalog for identifying explicit workflow skills.
- Move Root/user approval and worker-escalation behavior out of the skill and into project-level orchestration guidance.
- Keep the guide catalog aligned with the routing descriptions of the explicit skills it summarizes.

## 0.2.1 - 2026-08-23

- Tighten `workflow-guide` so the implicit advisory layer stays lean: keep the hidden explicit-workflow catalog, remove repeated explanation and examples, and make ordinary work the clear default.
- Align each catalog entry with the target skill's routing description so the root gets enough information to judge a recommendation without loading the explicit skill itself.
- Narrow the guide trigger to material workflow transitions and simplify the Codex default prompt without changing invocation policy.
- Shorten the optional `AGENTS.md` integration example to the Root/user decision boundary and delegated-worker escalation rule; the plugin still does not bundle project instructions.

## 0.2.0 - 2026-08-23

- Add `workflow-guide`, an implicit advisory skill that helps the root recognize when one explicit workflow may materially help without entering that workflow automatically.
- Keep all ten workflow-transition skills explicit-only; the guide recommends the nearest useful transition, asks the user first, and does nothing when ordinary work should continue.
- Make worker behavior explicit: workers may surface a candidate workflow to the root but do not prompt the user or expand their assignment unless already authorized.
- Document harness-aware approval semantics: approval does not bypass skill-invocation rules, and user invocation may still be required by the current harness.
- Add an optional Root-level `AGENTS.md` integration snippet in the README without bundling project instructions into the plugin.
- Extend the routing corpus with advisory and negative cases so the guide is tested for both useful recommendations and restraint.

## 0.1.9 - 2026-08-22

- Repair semantic drift found by the repo-wide v3.8 language review while keeping the broader plain-language rewrite intact.
- Restore `material` where it acts as a routing, consultation, scope, or authority threshold rather than as stylistic wording.
- Keep research focused on evidence relevant to the current question or decision, and narrow its trigger back to questions that materially depend on primary evidence.
- Tighten `DESIGN-IT-TWICE` so alternative generation is user-requested or justified by a material interface decision that cannot be resolved reliably without comparison.
- Restore bug-fix authorization wording, merge-conflict invariants, and project/user authority wording where v3.8 had become too broad or too project-specific.
- Add negative routing cases for routine repository inspection and glossary lookup, plus a boundary case that prevents `codebase-design` from implying automatic alternative generation.

## 0.1.8 - 2026-08-22

- Rewrite all 16 skill entry files for clearer, more direct engineering language while preserving routing, authority, stopping conditions, and workflow behavior.
- Stop `codebase-design` from imposing a private design dialect: keep deep-module concepts available when useful while preserving ordinary repository terms such as service, API, boundary, and component.
- Simplify supporting TDD, prototype, domain-modeling, and codebase-design guidance where abstract wording or categorical vocabulary could steer models toward unnecessary formalism.
- Simplify user-facing Codex skill descriptions and prompts so harness metadata uses the same plain-language boundaries as the skills themselves.
- Keep the 16-skill set, explicit/implicit invocation policy, routing cases, persistence model, and orchestration boundaries unchanged.

## 0.1.7 - 2026-08-22

- Make inherited `codebase-design` and TDD testing guidance proportional: deep-module, seam, mock, and interface-testing rules remain strong heuristics rather than universal laws.
- Separate bug diagnosis from permission to modify the implementation; `diagnosing-bugs` now fixes only when the current task authorizes a correction and otherwise reports the established cause and smallest credible fix.
- Clarify that handoffs must be accessible to the receiving context and are transition snapshots whose stale live state should be retired, replaced, or updated after consumption when necessary.
- Allow ordinary staging/marking of resolved paths as part of an authorized merge-conflict resolution while keeping continue, commit, abort, and merge-strategy decisions under governing project/user authority.
- Remove the unused human-in-the-loop debugging shell template.
- Add a lightweight routing-case corpus for preserving semantic boundaries and explicit/implicit invocation intent without introducing a routing framework.
- Re-evaluate the explicit-only set and retain the v3.6 invocation policy unchanged for this consolidation release.

## 0.1.6 - 2026-08-22

- Add `resolving-merge-conflicts`, an explicit-only procedure for reconciling Git conflicts from the intent and evidence behind both sides without forcing abort/continue/commit policy.
- Add `handoff`, an explicit-only transition procedure that compacts only live session state and points to existing durable work artifacts rather than duplicating them.
- Add `to-questionnaire`, an explicit-only procedure for obtaining missing decisions or facts from the external person who owns them without manufacturing answers or interrogating the wrong user.
- Apply the existing persistence, artifact-location, authority, and consultation principles to all three additions.

## 0.1.5 - 2026-08-22

- Clarify that persistence complements existing project artifacts and conventions rather than replacing them.
- Let existing project sources of truth, durable-state conventions, and governing consultation determine artifact location and authority.
- Keep local working state as an option for detailed or provisional cross-context state, not a preferred destination.
- Reframe Wayfinder maps as durable orientation state that may live in shared project artifacts, trackers, work documents, or local state.
- Replace canonical-map wording with a primary orientation artifact or view to avoid implying that Wayfinder must create project truth.

## 0.1.4 - 2026-08-22

- Add value-driven persistence for working state that needs to survive context compaction, fresh sessions, or handoffs.
- Prefer work-centered artifacts and existing work locations over skill-specific files or parallel folder trees.
- Make Wayfinder normally establish or reuse durable current state while keeping other skills conditional and proportional.
- Preserve compressed conclusions, evidence, status, and open questions rather than transcripts or append-only agent diaries.
- Keep local working state provisional unless it is deliberately promoted into shared project truth.

## 0.1.3 - 2026-08-22

- Rename `code-review` to `implementation-review` so the skill is clearly narrower than broader independent criticism.
- Make `implementation-review` explicit-only across Codex, GitHub Copilot CLI, and Claude Code.
- Clarify that passing implementation review never satisfies or cancels a broader independent-review checkpoint configured by the project.

## 0.1.2 - 2026-08-22

- Refine all skill descriptions as routing metadata so harnesses can distinguish adjacent skills before loading their bodies.
- Add explicit trigger conditions and semantic boundaries without changing skill workflows or invocation policy.

## 0.1.1

- Restore additive harness metadata without coupling skill behavior to a harness.
- Add Codex `agents/openai.yaml` presentation metadata and implicit-invocation policy for every skill.
- Mark workflow-transition skills explicit-only for Copilot CLI and Claude Code with `disable-model-invocation`.

## 0.1.0

- Extract the adapted engineering workflow into one focused plugin.
- Package the skills using Agent Plugins 1.0.0.
- Add marketplace support for Codex, GitHub Copilot CLI, and Claude Code.
- Separate the maintained product branch from the clean `upstream-main` mirror.
