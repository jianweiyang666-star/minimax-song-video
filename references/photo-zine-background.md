# Source-derived photo-zine backgrounds

Read this reference only when the user wants an author-supplied photo transformed into a tactile editorial, collage, torn-paper, or photo-plus-illustration background for a vertical lyric video. The background must support the song interface; it is not a standalone poster.

## Decision order

Resolve conflicts in this order:

1. Preserve the scene identity and its important spatial relationships.
2. Keep the photographic anchor truthful.
3. Reserve calm, readable regions for title, player controls, primary lyrics, and any translation.
4. Simplify repeated or noisy detail into a few large forms.
5. Let illustration and color grow from shapes already present in the photo.
6. Add paper texture and a torn transition without turning them into the focal point.

Preserve relationships before surface detail. Remove visual noise before adding decoration.

## Build a scene card

Inspect the actual photo and record a compact internal plan:

- **Anchor:** the one or two subjects that make the scene recognizable.
- **Context:** up to three supporting elements that establish place, time, or atmosphere.
- **Invariants:** horizon, facing direction, relative position, scale, path, silhouette, or overlap that must survive.
- **Dominant gesture:** the strongest horizontal, vertical, diagonal, curve, gaze, or convergence.
- **Visual weight:** where darkness, saturation, faces, texture, or edge tension already pull attention.
- **Native palette:** temperature, value range, dominant hues, and any meaningful minor color.
- **Source shapes:** one or two existing contours, shadows, paths, architectural rhythms, or atmospheric fields that can continue into illustration and color.
- **Quiet zones:** sky, water, wall, paper, haze, pavement, or another low-information area suitable for interface text.
- **Semantic minimum:** the fewest forms and relationships needed to still identify this particular scene.

Do not start the image prompt until the title and lyric regions have been assigned to quiet zones or protected by a planned local scrim.

## Select the transformation

Use the smallest intervention that solves the layout:

- **Crop and finish:** preserve the photo almost entirely; add only paper tone, restrained texture, and layout-safe grading.
- **Extended canvas:** keep the original photo region intact and generate only the missing 9:16 space.
- **Transformative seam:** keep one factual photo anchor and let a source-derived contour continue across a torn boundary into illustration.
- **Photo anchor with quiet field:** place the truthful scene in one strong region and use a larger, low-density illustration or paper field to create lyric space.
- **Underprint passage:** use a broad, subdued print field behind both photo and illustration when the image needs continuity without extra objects.

Avoid a default centered rectangle with empty decoration around it. Follow the source horizon, gaze, path, shoreline, shadow, or architectural direction.

## Build the abstraction map

For every non-photographic region decide:

- **Retain:** keep only defining forms or relationships.
- **Merge:** combine repeated trees, windows, railings, waves, crowds, or lights into one rhythm or mass.
- **Omit:** remove secondary objects, clutter, redundant contours, and texture that competes with lyrics.
- **Transform:** convert a selected source form into a silhouette, interrupted contour, cut-paper shape, halftone field, or sparse repeated mark.
- **Expose:** leave deliberate paper or atmospheric space inside and around the forms.

Choose one primary illustration grammar and at most one supporting grammar:

- broad silhouette for trees, figures, roofs, vehicles, or strong profiles;
- broken contour for architecture, paths, coastlines, or railings;
- low-density field for sky, water, fog, ground, or shadow;
- sparse rhythm for windows, posts, reflections, steps, or distant lights;
- cut-paper form when the source has a clear shape hierarchy.

The generated section must reinterpret the source rather than trace every object. It should still read clearly at thumbnail size.

## Compress complex detail

Complex photos require stronger simplification, especially around subtitle regions.

- Collapse dense foliage into one dominant canopy or tree mass, a few directional branch gestures, and at most two supporting clusters.
- Merge crowds, windows, city lights, gravel, rain, snow, waves, and reflections into grouped fields or interrupted rhythms.
- Preserve the characteristic lean, opening, direction, or light gap instead of individual leaves, panes, droplets, or faces.
- If the background reads like lace, engraving, visual static, or a full-scene tracing at thumbnail size, remove marks and enlarge quiet shapes.
- Keep fine texture near the photo-to-paper seam or one intentional pressure point; do not scatter it across the lyric field.

## Use color as structure

Add no more than one new print hue beyond the source photo and neutral paper/ink tones. Choose it by one of these relationships:

- intensify a meaningful minor color already in the scene;
- use a nearby hue for quiet harmony;
- use a restrained warm/cool counterpoint when the composition needs separation.

Attach the hue to a source-derived shape or direction. It may continue a road or roofline, replace part of a real region, sit beneath a photo/illustration seam, form a countershape from a shadow or gap, or repeat along a real path.

Perform a removal test: if deleting the added hue would not change balance, eye path, figure-ground separation, or photo-to-illustration continuity, redesign or remove it. Never add a detached bright rectangle, arbitrary dot, or generic brush swatch merely to make the frame look designed.

## Build the torn-paper handoff

Use a torn edge only where photography materially hands off to paper or illustration.

- Keep the contour irregular and asymmetrical, with a narrow warm fiber fringe and a few local abrasions.
- Let a source-derived illustration or color shape cross selected edge sections so the seam belongs to the composition.
- Keep speckles, halftone crumbs, or faded residue sparse and close to the seam.
- Keep the result flat like a scan. Avoid sticker borders, uniform deckled frames, heavy shadows, curled corners, or layered 3D paper depth.

The tear must remain visible without becoming a decorative frame or competing with the active lyric.

## Protect Remotion text

Do not ask the image model to render the song title, lyrics, translation, timecode, player controls, logos, or service chrome into the background. Those elements are added later in Remotion for accuracy and animation.

- Reserve at least one stable quiet zone for the active lyric and one smaller zone for title and controls.
- Keep faces, landmarks, and essential objects outside those zones when possible.
- If the source cannot provide calm space, use a paper field, low-density illustration, or planned translucent scrim rather than blurring the whole image.
- Carry only a background palette into Remotion. The final primary, translation, inactive, accent, outline, and scrim colors are chosen after the 9:16 background is complete.

## Prompt compiler

Compile the image-generation prompt into four concise parts:

1. **Canvas and attention geometry:** 9:16 flat background, photo/illustration allocation, focal anchor, quiet lyric regions, and eye path.
2. **Scene fidelity:** anchor, context, invariants, semantic minimum, and the original area that must remain photographic.
3. **Transformation:** retain/merge/omit/transform/expose decisions; primary illustration grammar; source-derived structural hue; torn-paper seam; paper and print behavior.
4. **Constraints:** preserve identity and natural photo color; no generated words or interface; no generic decoration, extra people, unrelated scenery, glossy mockup, 3D paper, logo, or watermark.

Include only instructions that can become visible pixels. Do not place file paths, analysis notes, or design-theory explanations in the final image prompt.

## Targeted correction

Inspect the result at normal size and thumbnail size. Regenerate at most once for the image-design stage, correcting only the observed failure:

- **Scene lost:** restore the missing invariant or source-specific form.
- **Too literal or busy:** merge forms, remove at least half the small marks, and enlarge quiet space.
- **Generic collage:** replace invented motifs with a contour, rhythm, shadow, or field extracted from the source.
- **Lyric area crowded:** reduce illustration density or replace it with paper/atmosphere; do not shrink the future lyrics to compensate.
- **Decorative color:** attach the hue to a source shape and give it a clear balancing or directional role.
- **Weak or fake tear:** restore an irregular narrow fiber transition and remove uniform outlines or heavy depth effects.
- **Photo damaged:** restore natural geometry, color, and recognizable detail in the photographic anchor.

## Quality gate

Before using the result in Remotion, verify:

- the supplied scene is still immediately recognizable;
- the anchor and key spatial relationship remain truthful;
- illustration simplifies rather than traces the photo;
- busy organic or repeated detail has been compressed;
- quiet space is intentional and sufficient for the actual lyric layout;
- illustration, color, and seam follow source-derived geometry;
- the single added hue performs a compositional function;
- the torn boundary reads as material without becoming a frame;
- no generated text, logo, player UI, watermark, or unrelated object appears;
- the image remains legible as a background at phone size.

## Source note

This independently written adaptation was informed by the scene-analysis and source-derived collage concepts in [Zeejay0's Gathered Scenes Zine skill](https://github.com/Zeejay0/gathered-scenes-zine-skill/tree/main/skills/scenes-gathered-zine-v1-3). No source assets or verbatim instruction blocks are included. The referenced repository is distributed under its own Personal Non-Commercial License; consult that repository before directly copying or using its original materials.
