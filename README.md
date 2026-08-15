# Logo Skills

Agent skills for designing premium, distinctive logos through structured concept routes, optional 3D rendering, image-generation workflows, and rigorous critique.

## Included skill

| Skill | What it does |
|---|---|
| [`logo-designer`](skills/logo-designer/SKILL.md) | Creates and refines mascot, object, abstract, monogram, and emblem logos with flat-first validation and optional 3D treatment. |

## Use it

Copy `skills/logo-designer` into an Agent Skills-compatible skills directory, then invoke it by name:

```text
Use $logo-designer to create three premium logo concepts for an AI accounting startup.
```

```text
Use $logo-designer to turn this sketch into a clean emblem and an optional enamel 3D presentation.
```

The skill stays focused on logos. It does not expand into a full brand system, general illustration, or UI icon family unless that scope is explicitly requested elsewhere.

## Design model

The five concept routes are mascot, object/pictorial, abstract symbol, monogram/letterform, and emblem. Rendering is a separate axis, so any suitable route can remain flat or receive a controlled soft-3D, glass, faceted, metallic, inflated, or enamel treatment.

The workflow requires an original concept thesis, a viable one-color mark, small-size inspection, text verification, and an explicit production-honesty check before delivery.

## Repository structure

```text
skills/logo-designer/
├── SKILL.md                 # workflow and route selection
├── SPEC.md                  # maintenance contract
├── SOURCES.md               # evidence and adaptation record
├── EVALS.md                 # trigger and decision-quality regression cases
├── agents/openai.yaml       # interface metadata
├── references/              # route and execution guidance
├── assets/                  # reusable brief and scorecard
└── scripts/                 # deterministic preview utility
```

Third-party logo images are not bundled. Public brands and galleries are treated as inspiration and negative similarity constraints, not copying targets.
