# Logo Designer maintenance specification

## Intent

Help an agent create distinctive, premium logos through route selection, structured generation, critique, and controlled refinement.

## Scope

In scope: logo briefs, five concept routes, wordmark and lockup decisions, optional 3D treatment, image-generation prompts, raster inspection, originality screening, and honest production handoff.

Out of scope: general illustration, UI icon sets, complete brand strategy, legal trademark clearance, and representing generated raster art as production vector work.

## Users and triggers

Use for founders, designers, marketers, and small-business owners asking to create, redesign, compare, or refine a company, product, app, service, or startup logo. Avoid triggering on adjacent illustration or icon-system work.

## Runtime contract

- Work from the user's brief and references without requiring a fixed provider.
- Use an available image-generation tool for exploration and editing.
- Inspect outputs before presenting them.
- Keep each concept in a separate generation call.
- Preserve user-owned source files and save variants non-destructively.
- Use deterministic tooling for exact text and SVG construction when practical.

## Architecture

Primary shape: reference-backed workflow process. Secondary mechanics: route selection, prompt chaining, asset templates, deterministic preview script, and validation loop.

`SKILL.md` owns the end-to-end workflow and routing. Five route references own concept-specific logic. Rendering, generation, critique, and examples are orthogonal references. Assets provide reusable templates; the script provides objective raster previews.

## Evidence

`SOURCES.md` records the evidence inventory, trust tiers, adaptations, coverage, and retrieval stopping rationale.

## Validation

- Validate Agent Skills structure and metadata.
- Confirm every routed path exists and remains one level below the skill root.
- Test the preview script on representative RGBA and RGB files.
- Exercise at least one mascot, abstract, monogram, and imitation-heavy brief after material workflow changes.
- Re-check trigger precision whenever the description changes.
- Use `EVALS.md` as the regression set for trigger boundaries and expected routing.

## Limitations

Image models can misspell text, invent details, imitate common visual priors, and produce geometry unsuitable for direct vectorization. Originality screening is qualitative, not a legal clearance process. A beautiful large rendering can still fail as a small logo.

## Maintenance

Keep provider-specific instructions in `references/imagegen-execution.md`. Update route references independently. Add examples only when they teach a reusable decision or repair. Do not bundle third-party logo files without explicit rights.
