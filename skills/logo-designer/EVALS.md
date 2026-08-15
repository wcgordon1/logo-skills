# Logo Designer evaluation cases

Use these cases after changing the frontmatter description, routing logic, or route references. They test intent boundaries and decision quality; they are not legal or image-quality benchmarks.

## Should trigger

| Query | Expected behavior |
|---|---|
| “Design a premium logo for an AI bookkeeping startup.” | Auto-route two or three distinct concepts; likely abstract, object, and monogram |
| “Create a cute but capable beaver logo for my plumbing company.” | Friendly-service mascot route; one trade cue; compact silhouette |
| “Make this approved flat mascot look softly 3D.” | Edit mode; preserve geometry; apply 3D treatment only |
| “Explore a symbol around a lighthouse for a cybersecurity company.” | Object route with a proprietary transformation, not a scene |
| “Give me an original SaaS logo with Linear-level restraint.” | Translate attributes; abstract route; explicitly avoid signature geometry |
| “Turn the initials AEJ into a premium mark.” | Monogram route; exact-letter and accidental-glyph verification |
| “Create a modern badge for a founders' community.” | Emblem route without heraldic or crypto-coin clutter |
| “Compare these three logo drafts and recommend one.” | Hard gates, weighted scorecard, specific recommendation and repair |
| “Redesign our logo from the attached sketch, keeping the silhouette.” | Edit mode with silhouette as an explicit invariant |
| “Make a symbol-only and symbol-plus-wordmark version.” | Treat lockups as output configurations, not new routes |
| “Create three genuinely different logo ideas, then refine the winner.” | Divergent theses first; one targeted change per later iteration |
| “Export the final logo in black, white, transparent PNG, and SVG.” | Verify alpha; provide SVG only if actually reconstructed and checked |

## Should not trigger

| Query | Reason |
|---|---|
| “Draw a detailed beaver working in a flooded kitchen.” | General scene illustration |
| “Create 24 navigation icons for a mobile app.” | UI icon family |
| “Build our complete brand strategy, messaging, and packaging system.” | Full brand engagement rather than logo work |
| “Remove the background from this product photo.” | General image editing |
| “Convert this approved logo into an `.ico` file without changing it.” | Mechanical favicon conversion with no logo decision |
| “Can we legally register this logo worldwide?” | Trademark/legal clearance |

## Adversarial and repair cases

| Query or failure | Expected safeguard |
|---|---|
| “Copy the Linear logo but replace the color and name.” | Refuse direct imitation; extract neutral attributes and change topology |
| Generated monogram reads `AJ` instead of `AEJ` | Fail hard gate; reconstruct or tightly edit exact letter geometry |
| 3D mark looks excellent but becomes a blob in black | Reject underlying concept; restore flat-first design |
| Five outputs are only palette changes | Do not call them concepts; change route, thesis, or silhouette |
| Mascot gains an extra paw during an edit | Repair only anatomy while locking pose, crop, and silhouette |

## Current v1 acceptance

- All five routes have an explicit selection rule, prompt scaffold, and repair guidance.
- 3D is consistently represented as an optional treatment.
- The workflow has negative imitation, text-accuracy, small-size, monochrome, and vector-honesty gates.
- Out-of-scope cases are named in both the trigger description and workflow boundaries.
