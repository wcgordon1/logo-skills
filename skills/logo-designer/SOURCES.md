# Source synthesis record

## Classification and architecture decision

This is a `workflow-process` skill with a reference-backed expert shape. It also uses a router for five logo types, prompt chaining for the design sequence, a validation loop, reusable assets, and one deterministic inspection script.

Adopted:

- a lean orchestrating `SKILL.md`
- five independent concept-route references
- 3D as a rendering axis rather than a sixth logo type
- a provider-neutral core with a replaceable ImageGen adapter
- flat-first and originality hard gates
- transformed examples rather than copied brand assets

Rejected:

- one giant prompt covering all routes, because it weakens divergence and repair
- script-backed generation as the primary shape, because aesthetic judgment is central
- embedding third-party logo boards, because they add rights and staleness risk
- a sixth wordmark route, because wordmark and combination mark are output configurations

Deferred:

- legal trademark-search integrations
- automated vector tracing or Bézier reconstruction
- a permanent benchmark image corpus, pending rights-cleared examples

## Evidence inventory

| Source | Trust | Confidence | Contribution | Constraint |
|---|---|---:|---|---|
| `/Users/williamgordon/.agents/skills/skill-writer/SKILL.md` and its synthesis, authoring, routing, validation, and output references | Local authority | High | Synthesis discipline, architecture selection, source ledger, output contract | Authoring guidance, not logo-domain expertise |
| `/Users/williamgordon/.codex/skills/.system/skill-creator/SKILL.md` and `references/openai_yaml.md` | Local authority | High | Skill structure, metadata, progressive disclosure, validation | Requires concise frontmatter and flat references |
| `/Users/williamgordon/.codex/skills/.system/imagegen/SKILL.md` | Local runtime authority | High | Current Codex image-generation execution behavior | Runtime-specific details can change |
| [OpenAI Codex sample ImageGen skill](https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/imagegen/SKILL.md) | Primary upstream | High | Generate/edit branching, prompt schema, inspection, targeted refinement | Adapted rather than copied; current runtime wins on conflicts |
| [Agent Skills specification](https://agentskills.io/specification) | Primary standard | High | Naming, metadata, directory, and progressive-disclosure requirements | Standard does not define logo quality |
| [AppIcons.store](https://www.appicons.store/) | User-selected inspiration | Medium | Dimensional neo-skeuomorphic app-icon vocabulary and polish target | Inspiration only; do not reproduce or bundle its work |
| [Stripe](https://stripe.com/) and [Linear](https://linear.app/) | User-selected inspiration | Medium | Premium startup restraint and geometric confidence | Extract attributes, not signature geometry |
| [AccountExecutiveJobs.com](https://accountexecutivejobs.com/) | User-selected inspiration | Medium | Monogram relevance from the user's discussion | Site may change; not a construction template |

## Source adaptation

### Image generation

Retained stable behavior: distinguish generation from editing, use one call per concept, describe reference roles, preserve edit invariants, inspect every output, refine one issue at a time, and report output paths and limitations.

Excluded volatile details: model names, unsupported flags, fixed locations, and hard-coded transparency behavior. The active runtime contract governs alpha handling; outputs must be checked rather than assumed transparent.

### Visual references

The inspiration set is translated into neutral attributes: high material polish, centered readable silhouettes, controlled lighting, confident geometry, and premium restraint. No third-party image is included in the repository. Famous brands are negative similarity constraints as well as quality references.

## Coverage matrix

| Requirement | Covered by |
|---|---|
| Brief framing and bounded scope | `SKILL.md`, brief asset |
| Five logo types | Five route references |
| Optional 3D | `rendering-3d.md` |
| Image generation and editing | `imagegen-execution.md` |
| Originality and negative examples | `critique-and-repair.md`, transformed examples |
| Exact text and vector honesty | `SKILL.md`, monogram reference |
| Small-size and monochrome checks | Critique reference, preview script |
| Repair and iteration | Critique reference, ImageGen adapter |
| Trigger precision | Frontmatter description, `SPEC.md` |
| Rights-aware sourcing | `SKILL.md`, this record |

## Retrieval stopping rationale

The sources now cover the format authority, runtime authority, all agreed logo routes, rendering treatment, originality behavior, validation, and maintenance. More reference scraping would mainly add visual examples rather than new operating rules. Retrieval should resume after output testing reveals a concrete gap or when a rights-cleared benchmark set is available.

## Known gaps

- No legal trademark clearance is performed.
- No rights-cleared benchmark corpus is bundled yet.
- Image-generation quality varies by provider and model.
- Production SVG reconstruction remains a manual or provider-specific step.
