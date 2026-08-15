# Quality Gate

Inspect the actual generated raster at full view and thumbnail size.

## Source Fidelity

- `scripts/preflight_source_image.py` passed on the exact supplied file before analysis or generation, or the brief records the client's explicit `low_resolution_override`.
- No Photos library, parent directory, database, UUID, iCloud asset, AppleScript, or UI automation was searched to locate a different source.
- A `blocked_thumbnail` never entered image generation or finalization. Do not claim high-resolution fidelity or social-ready sharpness for a low-resolution override.
- The top panel is recognizably the supplied photograph.
- Only crop and scale changed unless the user permitted more.
- No person, body, face, object, text, horizon, reflection, or lighting relationship drifted materially.
- Every source crop in the lower object remains faithful and unwarped.
- The delivered top panel uses original source pixels, not a model recreation.
- Fine source details remain sharp in the 2160×3600 working master and legible in the 1080×1800 review preview; inspect 3840×6400 only after explicit final approval.
- Any person or recognizable source fragment in the music object came directly from the supplied original, was uniformly scaled, and retained genuine overlaps and proportions.
- No artificial water ripple, embossed ripple, paper fiber, print grain, halftone, risograph, or filter was copied from the master or layered over the top photograph.
- The final `PHOTO_BOX` is pixel-identical to a direct EXIF-transposed, RGB-converted, crop-only LANCZOS fit of the supplied source.

## Metaphor

- The music object is readable at thumbnail size.
- At least three visible source features perform functional music roles.
- The object could not be swapped onto an unrelated photo without losing its logic.
- The result is not a stock music product plus pasted cutouts.
- The chosen device differs from recent visible outputs when another grammar fits equally well.

## Copy

- The client approved this exact proposition before image generation, unless they explicitly waived confirmation.
- The Chinese sentence is concise, natural, and contains one clear conceptual turn.
- The musical verb is meaningful rather than decorative.
- Exact text is readable and correct.
- No exact location, date, weather, BPM, or technical metadata was invented as fact.

## Song Match

- The song branch was resolved before image generation: either the client's exact title and artist were used without loading the bundled library, or the full bundled library was read and ranked.
- The selected song exists in the bundled 100-song Markdown library unless the user explicitly supplied another source.
- The match is supported by scene, emotional temperature, movement, light/color, and the user's listening evidence—not title coincidence alone.
- Song title and artist are exact. Every built-in match renders the table's verified duration; a client-supplied track renders duration only after verification.
- The song is not repeated across adjacent posters without intent.
- A clickable NetEase link with a plain numeric song ID is taken directly from the bundled Markdown row.
- No CLI or external music lookup ran during a normal built-in-library match.

## Composition

- The working master is exactly 3:5 and 2160×3600; the default client-review preview is exactly 1080×1800. A confirmed final delivery is exactly 3840×6400 at 300 DPI.
- The centered 3:4 information core remains at `y=360..3240`; the 3:5 sleeve adds 360 px above and below.
- The photo box is exactly `(62, 424, 2098, 2214)` or `2036×1790`, with 62 px side margins, divider at `y=2252`, and a 38 px photo-to-divider paper gap.
- Photo, divider, copy, object, and negative space form one hierarchy.
- The lower object is neither tiny nor edge-clipped.
- One source-derived accent remains visible at thumbnail scale.
- Paper, grain, and type share the same printed world.
- The lower music object does not touch the divider and keeps at least 54 px of paper breathing room.
- Circular objects are true circles; devices, people, earcups, reels, and labels are not stretched.
- A vinyl/CD/cassette reel's outer body, label/reel, and spindle/hub share one computed center. Reject any non-zero center offset.
- The lower-left proposition, track, artist, and playback line are exact deterministic typography.
- The left column visually matches `assets/layout-master-3x5.png`: large Songti proposition, compact monospaced song/artist block, outlined circular play button, photograph-derived accent progress knob/completed segment, grey remainder line, both endpoint timestamps for built-in tracks, and bottom archive row. Reject small body-copy styling, a bare triangle, a missing built-in duration, or ad-hoc vertical spacing.
- The lower half is one uninterrupted paper surface. Reject any rectangle, tonal seam, card, wash, or separate backing color behind the left typography zone, even when the difference is subtle.
- The added sleeve is either empty or uses only the approved micro-label, edition, registration mark, and bottom hairline/dots. Reject unexplained ripples, embossed patterns, gradients, extra copy, or visual clutter.

## Reject and Retry Once

Retry with tighter constraints if any is true:

- the main photo was repainted or content changed;
- the Chinese text is wrong;
- fewer than three source mappings survive;
- the music object is generic, malformed, or visually ambiguous;
- people or recognizable objects are stretched;
- the result becomes glossy advertising, a full-bleed scene, or a busy scrapbook;
- the composition merely repeats the previous poster without photographic reason.
- the file is not exact 3:5, the original photo is blurry or redrawn, a circle is elliptical, a label/hub is off-centre, or the object touches the divider;
- the track information is guessed, misspelled, or mismatched to the photograph.
- the left typography sits on a visibly different paper patch or colored panel.
- master-photo texture was mistaken for a series style and added as water ripples, embossing, grain, paper, halftone, risograph, or any other overlay on a later top photograph;
- photo margins or frame coordinates were estimated visually instead of using the locked grid;
- the lower information, player, paper, or music object was regenerated or changed merely to repair the source crop;
- a lower music object touches or crosses the divider or keeps less than 54 px of paper breathing room;
- a portrait or other source was stretched instead of cropped proportionally;
- original-photo fidelity is claimed without passing pixel-level assertions.
- source preflight is missing, a Photos thumbnail was silently accepted, or a low-resolution override was inferred rather than explicitly approved;
- the image-generation canvas or art base is presented as the completed preview;
- the art base was mislabeled as the finished poster, or the art base and final preview appeared in the same assistant turn;
- finalization began before the client replied Continue after seeing the art base;
- the final preview was delivered only as a tool attachment, canvas item, thumbnail, filename, or download link instead of a large inline Markdown image;
- the final preview Markdown target was relative, non-local, or not the exact verified 1080×1800 PNG;
- the final-preview turn contained any additional image or screenshot;
- Luna was recommended as the default production model, or Terra's `70%–80%` visual estimate was misrepresented as Token savings;
- an exact Token count was promised without a reliable measured source.

## Final production assertions

During the default review stage, inspect the 1080×1800 client preview at full
view and thumbnail size, and run deterministic checks on the 2160×3600 working
master: canvas, 3:5 ratio, direct-source `PHOTO_BOX` equality, object aspect
ratios, and shared centers for every concentric component. Do not create a 4K
file before approval. After explicit approval, additionally assert 3840×6400
dimensions, 300 DPI, and direct-source high-resolution `PHOTO_BOX` equality.
For an approved-poster photo
repair, additionally assert that every pixel at `y>=2214`, the sleeve, and both
photo side margins remains identical to the approved base. Do not report
completion when any assertion is missing or fails.

Before review delivery, assert the visible-base boundary from `approved-brief.json`:
the previous turn showed the art base and ended at `art_base_ready`; the client then replied Continue; the current turn made no image-generation call; `--out-quick` succeeded; and the exact 1080×1800 PNG is embedded once with `![最终预览](/absolute/path.png)` as the only image in the response. Include a separate clickable download link to the same absolute path. Reject delivery if the preview is merely an attachment/thumbnail or if the client UI would receive a multi-image gallery.

Reject a workflow that calls image generation or exports 4K for a copy-only,
song-only, metadata-only, accent-only, progress-only, or crop-centering revision.

If the second attempt still breaks preservation, return the better result and state the limitation honestly.
