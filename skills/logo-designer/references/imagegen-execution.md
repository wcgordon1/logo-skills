# Image-generation execution adapter

Use the active environment's image-generation capability. Runtime-specific tool instructions take precedence over this reference.

## Choose the mode

- **Generate** when no source image must remain invariant.
- **Edit** when changing an existing logo, refining an approved concept, or preserving exact geometry, composition, or identity.
- If reference images are supplied, label each role: content reference, style attribute, composition reference, or source to edit.

## One concept per call

Use a separate call for every distinct asset or concept. Do not request a contact sheet of unrelated alternatives as one generated image. Separate calls make the prompt, result, critique, and revision traceable.

## Structured prompt

Build prompts in this order:

```text
Purpose: logo exploration for [brand and use].
Route and subject: [mascot/object/abstract/monogram/emblem plus concept thesis].
Construction: [silhouette, topology, geometry, negative space, detail budget].
Brand signal: [two or three attributes].
Color: [limited direction]; must also work in one color.
Composition: centered, isolated mark, readable at [smallest size].
Rendering: [flat vector-like or approved 3D treatment].
Text: [none, or exact verified text].
Preserve: [edit-only invariants].
Exclude: mockups, scenes, watermarks, stock-icon cliches, famous-logo resemblance,
unrequested objects, and arbitrary decorative effects.
```

Keep user specificity. Do not invent slogans, animals, symbols, colors, or typography simply to make a prompt longer.

## Inspect every result

After generation or editing:

1. open the actual output,
2. check the requested route and concept thesis,
3. inspect silhouette, text, anatomy, negative space, and artifacts,
4. compare against references for accidental imitation,
5. run small-size and monochrome checks,
6. decide whether to accept, repair, or change route.

Do not present an uninspected output.

## Controlled refinement

Make one targeted change per iteration. State what must remain invariant. If an edit repeatedly drifts, return to the last accepted output or reconstruct deterministically.

## Output handling

- Save variants non-destructively with clear concept and revision identifiers.
- Record which prompt produced each output.
- Follow the active runtime's current transparency workflow; request alpha only when supported and verify the resulting channel.
- Do not promise editable SVG from a raster generator.
- Report the mode used, files produced, and any unresolved defect.
