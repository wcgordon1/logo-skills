# Monogram or letterform route

Use a monogram when one to three initials can become the main recognition device. Treat letters as exact information and custom geometry—not as text decoration.

## Construction

- Confirm the required letters, order, capitalization, and pronunciation.
- Choose a relationship: interlock, shared stem, ligature, container, overlap, or negative-space reveal.
- Preserve at least one unmistakable cue for every required letter.
- Customize a small number of structural details rather than distorting every stroke.
- Balance counters, stroke weight, and spacing in one color.
- Test whether the mark creates an unintended extra glyph or symbol.

Use image generation for exploration only. Rebuild promising letterforms with deterministic vector geometry before calling them final.

## Prompt scaffold

```text
Explore an original monogram logo using exactly the letters [LETTERS] in that order.
Brand signal: [traits]. Letter relationship: [construction move].
Distinctive feature: [specific shared stroke/counter/negative-space idea].
Construction: custom letterforms, balanced counters, bold silhouette,
one-color viability, readable at 16 px.
Exclude: extra letters, mirrored accidental glyphs, illegible overlap,
off-the-shelf font treatment, decorative mockup, and resemblance to known monograms.
```

## Verification

Manually inspect:

1. every letter and its order,
2. counters and joins at full size,
3. recognition at 16–32 px,
4. accidental glyphs in rotation or reflection,
5. black and reversed-white versions.

If generated text is wrong, do not repeatedly ask the model to fix spelling in a complex render. Reconstruct the letter geometry or isolate the correction in a tightly constrained edit.
