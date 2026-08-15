# Design and Prompt System

## Series Identity

- Vertical 3:5 Xiaohongshu poster, internal working master 2160×3600 PNG, default client-review preview 1080×1800 PNG, and confirmed final output 3840×6400 PNG at 300 DPI.
- Warm ivory or location-responsive archival paper with fibers, dust, fine grain, and matte absorption.
- Large original-pixel travel photograph above, conceptual music object below by default.
- Thin divider rule, sparse Chinese editorial copy, tiny monospaced archive labels.
- One main accent sampled from the photograph; secondary colors remain subordinate.
- Flat orthographic scan, xerox softness, film or risograph grain; no glossy mockup depth.

## Layout Families

Choose based on the photo rather than repeating coordinates.

### Split sleeve — default series layout

Use the exact locked production grid below. Do not express or estimate the
default photo/object split as a percentage. Keep the lower object visually
large while respecting the divider breathing gap and fixed photo box.

### Gatefold stereo

Two original photos or two source fragments occupy upper-left/lower-right. Use only for a genuine pair, duet, echo, before/after, or left/right relation.

### Album-window

One photo crop fills a jewel-case, booklet, cover, or playback screen form. Use for windows, pools, framed scenes, and strong rectangular geometry.

### Track-strip

Keep one large photo and let a path, river, train line, light streak, or row cross the paper as a tape or waveform. Use when the source has directional energy.

### Specimen object

Use a smaller photo panel and one isolated source-built device. Reserve for unusually clear object mappings and large negative space.

## Source Preservation

The approved master controls proportion, grid, typography, playback UI,
information hierarchy, and spacing only. Texture visible inside the master's
example photograph is not a reusable series treatment.

Before analyzing the photograph, run `scripts/preflight_source_image.py` on the exact supplied path. Do not search a Photos library or resolve an asset UUID. Treat a short edge below 1000 px as a blocked thumbnail by default, including common Photos derivatives such as 360×480 or 360×540. A Photos derivative that meets the pixel gate may proceed. Continue with a smaller file only after the client explicitly accepts reduced sharpness; 4K export must never be described as detail recovery.

In the main photo panel:

- only crop and scale;
- preserve identities, bodies, object count, lettering, lighting, geometry, perspective, and color relationships;
- do not use generative fill to “complete” a crop;
- do not remove inconvenient foreground objects;
- do not replace skies, water, buildings, plants, or people.
- use the original full-resolution file for the final top panel; never upscale a model-redrawn photo when the source is available.
- apply only EXIF transpose, crop, scale, and LANCZOS resampling before direct pixel backfill;
- do not add artificial water ripples, embossed ripples, paper texture, grain masks, risograph/halftone texture, filters, color grading, or any “unified print texture” over the top photograph;
- preserve naturally photographed water shimmer and all other source texture exactly as part of the original photograph;
- completely overwrite the generated art base inside `PHOTO_BOX`; no generated photo pixels may remain in the production file.

In the conceptual object:

- allow clipping, masking, circular or rectangular crops, repetition, rotation of texture-only fragments, halftone, and paper edges;
- never stretch a person or recognizable object to fit a device part;
- preserve source lettering if visible, but do not promote accidental brand text into poster branding;
- use illustration only for neutral connective hardware such as a fine tonearm, rail, hinge, shell, wire, or label border.

## Typography

- Treat `assets/layout-master-3x5.png` as the binding series master for grid, type hierarchy, player styling, sleeve extensions, and visual density. Its expected SHA-256 is `6063fa94417c14c2853ec23c8d514abe61f8ff6d0e0d8723301e46647ecbe355`. Inspect it when changing the finalizer or judging a final poster.
- Chinese proposition: 1–2 short lines in Songti SC Regular, approximately 82 px on the 2160×3600 master. It is the dominant lower-half typography, not small editorial body copy.
- Allow one short phrase to receive a pale halftone rectangle in the photograph-derived accent color; keep the type itself black. Use at most one highlight per poster and omit it when no phrase deserves emphasis.
- Metadata: 2–4 lines, monospaced or typewriter face.
- Keep text secondary to image and metaphor.
- Render the proposition verbatim. If generation corrupts it, retry once with shorter copy and stronger exact-text instruction.
- No commercial headline, CTA, fake campaign logo, or decorative English paragraph.
- Place the song title and artist below the proposition in small uppercase monospaced display type (Chinese and other uncased scripts remain unchanged). Below them use the master player: a black play triangle inside a thin outlined circle, photograph-derived accent knob and short completed segment, long grey remainder line, `00:00` under the left end, and verified duration under the right end. Built-in tracks always supply duration; a client-supplied unverified duration may remain blank. Put the archive/location line near the bottom margin.

## Production Grid

Lock these exact coordinates on every default series poster. Do not visually
estimate them or drift back to percentage-based placement. Use another layout
only when the user explicitly requests it:

- working master: `2160×3600` PNG, strict `3:5`;
- default client-review preview: `1080×1800` PNG, generated from the verified working master;
- confirmed 4K delivery: `3840×6400` PNG at 300 DPI, generated only after explicit approval;
- centered 3:4 information core: `y=360..3240`; the 3:5 sleeve adds exactly 360 px above and 360 px below;
- upper photo box: `(62, 424, 2098, 2214)`;
- upper photo size: `2036×1790`;
- left/right photo margins: `62 / 62 px`;
- upper photo top: `424 px`;
- divider: `y=2252`, from `x=62` to `x=2098`;
- paper gap from photo bottom to divider: `38 px`;
- lower-left blank typography zone: `x=120, y=2340, width=760, height=830`;
- lower-right conceptual object zone: `x=920, y=2320, width=1120, height=800`;
- minimum divider-to-object breathing gap: 54 px;
- safe edge for all critical text and object silhouettes: 62 px.

The extended sleeve has only two modes:

- `plain`: extend the same unbroken paper above and below; add nothing;
- `restrained`: at most a top-left micro series label, top-right `3:5 EDITION`, one small registration cross, and one bottom-right hairline with three accent dots.

Do not add artificial ripples, embossed patterns, extra paper texture, decorative gradients, large symbols, or extra copy in the sleeve. The reference's existing paper is the background; never manufacture a new texture layer over it.

Generate the art base without lower-left text. The deterministic finalizer adds copy and playback information. Do not place the music object inside the typography zone. The entire lower half must remain one continuous paper field: never add a rectangle, card, wash, patch, panel, or separate background behind the left text column.

Do not improvise a new left-column style per poster. The approved master fixes the relative hierarchy: large Songti proposition, two compact song lines, circular player row, then one bottom archive line. Any purposeful object variation happens on the right; the left-side music information remains series-identical.

The finalizer must not clear or repaint the reserved typography zone by default, because doing so creates a visible paper-color seam. If generated copy leaks into that zone, regenerate the art base with a stronger blank-zone instruction instead of covering it with a paper patch. The finalizer may still normalize the narrow breathing gap between the original-photo box and divider.

Never stretch a near-3:5 generated image to fit. Pad or crop paper only. Any record, CD, reel, circular label, center hole, headphone cup, or device control must keep its geometric aspect ratio. For concentric objects, compute the outer body, inner label/reel, and spindle/hub from one shared `(cx, cy)` and assert a `(0, 0)` center offset. Do not use a photo fragment as a record label unless the concept explicitly requires it. Place source-derived people outside the label when the metaphor calls for figures on the grooves; extract them only from the original photograph with one uniform scale factor per crop.

## Approved-poster photo repair

When the user asks only to fix crop, ratio, sharpness, or original-photo fidelity
on an already approved poster, freeze the entire base outside `PHOTO_BOX`. Do not
regenerate the poster or re-typeset the lower information. Run
`scripts/backfill_original_photo.py` with the approved poster as `--base`, the
original image (or a temporary HEIC conversion) as `--source`, and explicit
`--center-x/--center-y` values. Accept the result only after its built-in canvas,
photo-box, lower-region, and margin pixel assertions pass.

## Prompt Shape

Write four decisive blocks:

1. **Canvas and layout:** strict 3:5, centered 3:4 core, sleeve mode, production grid, paper, margins, divider, blank lower-left zone, object location.
2. **Photo contract:** edit-target role, high preservation invariants, crop/scale permission only.
3. **Metaphor construction:** one object and at least three explicit source-feature mappings; selected-song atmosphere; accent hue and print treatment. Reserve exact text for deterministic typesetting.
4. **Mood and avoids:** flat scanned zine mood plus the shortest relevant negative list.

Always state: “The conceptual object must feel distilled from this exact photograph, not a stock music product pasted beside it.”

## Default Avoids

Generic musical notes, treble clefs, random piano keys, equalizer decoration without source evidence, stock black vinyl, arbitrary CD rainbow, dry cutouts, warped people, altered main photo, invented subjects, repeated use of the previous poster's device, glossy 3D product rendering, hard shadows, neon, commercial ads, brand logos, dense scrapbook clutter, fake location/date, long text, watermark.

Also avoid: 3:4, 9:16, or 2:3 output unless explicitly requested, stretched adaptation, ellipse instead of a circle, off-centre label/hub, model-redrawn top photo, fuzzy original details, music object touching the divider, unverified duration, invented song spelling, generated text in the reserved lower-left zone, any visible rectangular backing color behind the left text column, copied master-photo water texture, artificial water ripples, embossed photo texture, paper/grain/halftone overlays on the top photograph, visually estimated photo margins, decorative sleeve clutter, and regenerating the lower design merely to repair a crop.
