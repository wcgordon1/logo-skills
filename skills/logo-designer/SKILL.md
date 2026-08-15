---
name: logo-designer
description: Designs and refines distinctive professional logos from briefs or reference images, including mascot, object/pictorial, abstract symbol, monogram/letterform, and emblem routes; optional flat, dimensional, or 3D treatments; wordmark and combination-mark exploration; image-generation prompting; critique; and originality checks. Use when a user asks to create, generate, redesign, compare, or improve a company, product, startup, app, service, or small-business logo. Do not use for general illustrations, UI icon sets, or full brand-strategy projects.
---

# Logo Designer

Create a memorable logo through divergent concept routes, flat-first validation, controlled image generation, and explicit critique. Stay strictly within logo design unless the user expands the scope.

## Operating principles

- Separate the **concept route** from the **rendering treatment**. Mascot, object, abstract, monogram, and emblem are routes; 3D is an optional treatment.
- Establish a defensible flat mark before applying depth, glass, metal, lighting, or texture.
- Generate genuinely different ideas before polishing one. Do not present recolors as concepts.
- Treat famous logos as attribute references, never tracing targets. Extract qualities such as restraint, geometry, or dimensionality and create original structure.
- Prefer a bold silhouette, one focal idea, limited internal detail, and strong recognition at small sizes.
- Do not claim that an image-generated raster is production vector artwork. Reconstruct clean SVG geometry when practical.
- Do not silently expand into naming, messaging, typography systems, packaging, or a complete brand identity.

## Workflow

### 1. Frame the brief

Extract what is already known before asking questions:

- exact brand name and any required initials
- product, audience, and category
- desired personality and premium level
- required or forbidden symbols
- competitor or visual references and the attributes they represent
- intended uses and smallest important display size
- desired output: symbol, wordmark, or combination mark
- preferred route and treatment, if any

Ask only the few questions whose answers would materially change the design. If the brief is incomplete but workable, state assumptions and continue. Use `assets/logo-brief-template.md` when a reusable brief artifact is useful.

### 2. Choose concept routes

If the user specifies a route, follow it. Otherwise choose two or three routes that express different brand strategies; do not force all five into every project.

| Route | Choose when | Load |
|---|---|---|
| Mascot | Character, warmth, trust, memorability, or a service-business personality matters | `references/route-mascot.md` |
| Object | A concrete noun or category-adjacent object can become a proprietary symbol | `references/route-object.md` |
| Abstract | The brand needs a scalable, ownable symbol not tied to a literal object | `references/route-abstract.md` |
| Monogram | Initials are short, distinctive, and useful as the primary recognition device | `references/route-monogram.md` |
| Emblem | Containment, belonging, authority, craft, or a badge-like composition is valuable | `references/route-emblem.md` |

Default to **auto-route** when no type is named. If two interpretations are equally plausible and would produce materially different outcomes, ask one concise question. If early concepts reveal a misroute, reclassify before polishing.

### 3. Define the concept before rendering

For each selected route, write a one-sentence concept thesis containing:

1. the recognizable visual idea,
2. the intended brand signal,
3. the distinctive structural move.

Then specify construction: geometric, organic, modular, negative-space, or custom-lettered. Reject concepts that depend on tiny details, effects, or a verbal explanation.

When producing a concept set, vary the underlying idea and silhouette. A useful default is three concepts from two or three routes. Preserve the user's constraints across every concept.

### 4. Set the rendering treatment

Default to flat vector-like presentation. If the user requests 3D—or it materially helps the exploration—load `references/rendering-3d.md` and choose one treatment such as soft 3D, glass, faceted, metallic, inflated, or enamel.

Never use 3D to rescue a generic mark. Validate the same mark in one color first, and keep a flat companion version.

### 5. Generate or construct

When image generation is available, load `references/imagegen-execution.md`. Generate each distinct concept in a separate call so prompts and outputs remain attributable. Clearly label reference-image roles and preserve exact invariants during edits.

Image generation is strongest for exploration, rendered mascots, objects, and 3D treatments. For exact letterforms, wordmarks, and final SVG geometry, use deterministic drawing or careful reconstruction when available. Verify every character manually; never trust generated spelling by default.

### 6. Critique and repair

Load `references/critique-and-repair.md`. Inspect every output, including at small size and in monochrome. Apply the hard gates before subjective scoring:

- correct brand text or initials
- recognizable silhouette
- no dependence on 3D effects
- no confusing resemblance to a famous or competitor mark
- no stock-icon, generic-AI-blob, or category-cliche result
- no unintended symbols, limbs, glyphs, or visual artifacts

Score viable concepts with `assets/logo-scorecard.json`. Repair one failure at a time. Preserve successful invariants and avoid broad prompts that cause concept drift.

For an objective raster preview, run:

```bash
python scripts/create_logo_preview.py INPUT_IMAGE --out OUTPUT_IMAGE
```

This utility exposes small-size, light/dark-background, and grayscale behavior; it does not make aesthetic judgments.

### 7. Deliver the decision

Lead with the recommended concept and explain why it wins in plain language. Include:

- route, concept thesis, and rendering treatment
- flat color, black, and white versions when production files are requested
- optional 3D presentation as a companion, not the only master
- symbol-only and combination lockups when applicable
- transparent PNG exports when alpha is verified
- clean SVG only when the geometry has actually been reconstructed and checked
- a concise note on originality risk and any unresolved production limitations

When the user wants more exploration, change the concept thesis or route. When the user wants refinement, preserve the thesis and make one targeted change.

## Wordmarks and lockups

Wordmark-only and symbol-plus-wordmark are output configurations, not additional concept routes. Keep typography subordinate to the core recognition idea unless the wordmark itself is the logo. For generated text, verify spelling, letter order, counters, spacing, and accidental ligatures at full resolution.

## Reference handling and rights

Use references to infer attributes such as softness, confidence, density, geometry, material, or composition. Do not reproduce protected marks, characters, or signature geometry. If a request is imitation-heavy, translate it into neutral design attributes and disclose that redirection. This workflow reduces obvious resemblance; it is not trademark clearance or legal advice.

## Examples

Load `references/transformed-examples.md` for a mascot small-business brief, a premium abstract startup brief, and an imitation-heavy anti-pattern with a corrected workflow.

## Boundaries

Do not use this skill for:

- general illustration, character sheets, or scenes
- interface icon families or toolbar symbols
- full brand-strategy or identity-system engagements
- mechanical favicon conversion when no logo decision is involved
- legal trademark searches or clearance opinions

Offer a narrow next step if the request crosses one of these boundaries.
