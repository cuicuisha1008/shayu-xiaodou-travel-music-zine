---
name: travel-music-zine
description: Turn user-supplied travel, street, architecture, landscape, or people photographs into 3:5 Xiaohongshu-ready Chinese music-metaphor zine posters. Use when Codex should distill a source-specific music object, present three copy options and ask for a preferred song before generation, optionally match from the embedded 100-song duration-complete library, recommend Sol or Terra with time guidance, show the generated art base for review, then after one Continue reply deliver the finished preview as a large inline image, and export 4K only after approval while preserving original photo pixels and exact geometry.
---

# 鲨鱼小豆 · Travel Music Zine

Create music × travel ZINE posters whose metaphor, copy, music object, and track grow from the photograph. Begin by reading the image, not by choosing a music product or song title.

## Progressive resource routing

Read only the resources required for the current stage:

1. Before viewing or analyzing the photo, run `scripts/preflight_source_image.py` on the one supplied file. Stop on a blocked thumbnail. After it passes, read `references/metaphor-system.md` completely.
2. Before the first client reply, read `references/copy-system.md` and `references/model-and-progress-guide.md` completely. Choose one metaphor, present three copy options, ask about the song, explain that the art base will be shown next and will require one Continue reply, then stop and wait.
3. If the client supplies an exact song title and artist, preserve them and **skip** both `references/song-matching.md` and `references/travel-song-library.md`.
4. If the client supplies no song, read `references/song-matching.md` and the complete `references/travel-song-library.md`, then select one embedded track.
5. After copy and song are resolved, read `references/approved-brief.md`, write the per-task `approved-brief.json`, generate and show the art base, then stop and wait for “继续生成最终预览”.
6. Read the locked brief, then read `references/design-system.md` completely and inspect `assets/layout-master-3x5.png` as the binding visual reference.
7. Before delivery, read `references/quality-gate.md` completely.

When a task resumes with a valid `approved-brief.json`, treat it as an execution-only handoff: skip metaphor ideation, copy proposals, song selection, and the full song library. Do not reinterpret locked fields. Route by `execution.status`: `approved` means generate and show the art base; `art_base_ready` plus “继续生成最终预览” means finalize without image generation; `preview_ready` means handle review or deterministic corrections.

Use built-in image generation only for the conceptual music object and blank-paper art base. Use `scripts/preflight_source_image.py` before any analysis or generation, `scripts/assert_concentric_geometry.py` for nested circular objects, and `scripts/finalize_poster.py` for exact 2160×3600 composition and the required 1080×1800 review preview; request 3840×6400 300-DPI output only after approval. Use `scripts/backfill_original_photo.py` for crop/fidelity-only repairs to an approved poster. If HEIC cannot be viewed, convert a temporary copy only; never modify the source.

## Workflow

### 1. Inspect the photograph

Before the checkpoint-0 notice, analysis, song-library reading, image generation, or task-brief creation, run:

```bash
python3 scripts/preflight_source_image.py /absolute/path/to/the-supplied-image
```

Inspect only that exact file. Never scan a Photos library, its parent folders, a Photos database, asset UUIDs, iCloud, or unrelated files; never use AppleScript or UI automation to locate another image. A path under `.photoslibrary/resources/derivatives/` is evidence that Photos supplied a cached derivative, but block based on actual dimensions: the default minimum short edge is 1000 px. A derivative that meets the dimension gate may continue normally.

If preflight returns `blocked_thumbnail`, stop before creative work and tell the client:

`我收到的是相册生成的 {width}×{height} 预览图，不是适合成稿的高清文件。请先从「照片」App 把照片拖到桌面，或使用「文件 → 导出」导出 HEIC/JPG，再上传桌面上的文件。重新上传后会继续当前任务，不需要重复确认文案和歌曲。`

Do not imply that 4K export can restore detail. If the client explicitly says the low-resolution file is the only available source and accepts blur, rerun preflight with `--allow-low-resolution`, record the override in the approved brief, and describe both review and 4K sharpness honestly. Never infer consent from “继续”.

After preflight passes, send the checkpoint-0 start notice from `references/model-and-progress-guide.md`. State what this turn will deliver, the current model's range, and the total active-work range to a quick preview. Explain that the client will confirm copy/song, then later reply Continue once after seeing the art base. Do not wait after this notice; continue inspecting the photograph.

Treat every supplied photo as a high-preservation edit target. Record dimensions/orientation when available, people, objects, architecture, landscape, light, color, repeated shapes, lines, gaps, reflections, shadows, and visible text. Preserve identity, pose, proportions, object count, geometry, perspective, lettering, lighting relationships, and recognizable color.

The main photo panel permits only EXIF transpose, proportional crop, scale, RGB conversion, and LANCZOS resampling unless the client explicitly permits more. Never synthesize, repaint, relocate, remove, stretch, beautify, recolor, filter, or texture it. Master-photo texture is not a transferable style.

### 2. Choose one source-derived music metaphor

Privately create three candidates. Map at least three visible source features to three functional music roles for each. Score source specificity, emotional fit, thumbnail readability, preservation feasibility, and freshness; choose one yourself and tell the client. Do not ask them to choose the metaphor.

Before choosing, review the current task's last three visible posters or confirmed concepts. Avoid repeating their music object, track, and main musical verb when another photograph-specific grammar fits. This is a current-conversation freshness check, not stored cross-client profiling.

Reject candidates that work only because a generic vinyl, note, CD, or headphone could be pasted beside any photo. Vary among record, cassette, CD, stereo channels, waveform, sampler, recorder, score, signal path, sleeve, speaker, and other genuinely source-supported grammars.

### 3. Confirm copy and song before generation

Follow `references/copy-system.md`:

- state the chosen metaphor and three short feature → music-role mappings;
- present exactly three Chinese propositions for the same metaphor and recommend one;
- ask whether the client has a desired song, requesting `歌名 + 歌手` if yes;
- if not, explain that the Skill will auto-match from its embedded 100-song library and summarize its current styles, scene range, languages, and verified durations;
- explain that this confirmation starts art-base generation; if the client wants Terra, tell them to switch before sending it; after viewing the art base they will reply Continue once for the final preview;
- stop and wait for the client's copy choice and song decision.

Do not read the full song library, inspect the layout master, call image generation, or make a preview before this confirmation. If the client explicitly says to proceed without confirmation, use the recommended copy.

### 4. Resolve the song with the cheapest valid branch

**Client-specified branch:** use the exact supplied title and artist. Do not read the song-matching guide or embedded library. Ask for the artist only when the title is ambiguous. Do not start NetEase CLI or guess duration.

**Embedded-library branch:** read `references/song-matching.md` and the full `references/travel-song-library.md`. Rank by scene, light, motion, intimacy, openness, nostalgia, temperature, energy, confidence, and comment-derived evidence. Keep three finalists privately and select one. Use the table's exact title, artist, atmosphere tag, verified duration, and numeric NetEase link. Do not re-fetch it through CLI.

Invoke `netease-music-cli` only when the client explicitly requests live search, playback/control, exact duration, or playlist refresh. For a series, avoid adjacent track, artist, and atmosphere-family repetition when the photos allow.

### 5. Lock the approved brief

After the client confirms copy and song, follow `references/approved-brief.md` and write `approved-brief.json` in the task's working directory. The file is the execution contract across model changes. Send the art-base start notice from `references/model-and-progress-guide.md`, then continue in the same turn.

Recommend **5.6 Sol** for the strongest metaphor and material quality, **5.6 Terra** as the acceptable faster compromise, and **do not recommend Luna**. Do not promise an exact Token count; provide relative consumption and the measured-style time ranges from the guide. Any model used after a switch must read the brief and continue without re-opening the song library or proposing new creative directions.

### 6. Build one music object from the source

After confirmation, read the design system and inspect the 3:5 master. Default production geometry is fixed:

- working master `2160×3600`; review preview `1080×1800`; approved 4K final `3840×6400` at 300 DPI;
- photo box `(62, 424, 2098, 2214)` = `2036×1790`;
- divider `y=2252`, leaving 38 px below the photo;
- proposition/song/player at lower left; one large conceptual object at lower right;
- the object stays at least 54 px below the divider;
- one continuous paper field, generous negative space, one photo-derived accent.

Keep the approved left-column hierarchy fixed: large regular Songti proposition, optional single accent-color halftone word highlight, accent-color `NOW PLAYING`, 36 px monospaced song title, smaller artist, outlined circular play button, accent-color progress knob/completed segment, grey timeline, both endpoint times for built-in tracks, and archive row. The accent follows the photograph; it is not forced to blue. Never place a colored card or separate backing behind the column.

Use source crops, masks, repetition, and geometric reassembly in the lower object. Let visible source elements become actual reels, grooves, channels, track marks, label, waveform, mesh, controls, or signal path. Preserve people and recognizable objects under uniform scaling. If a specific device is named, use accurate geometry without logos. Circles remain circles; outer body, label/reel, and spindle/hub share one computed center.

### 7. Generate and show the art base

Prompt image generation with:

- the locked 3:5 layout and blank lower-left/sleeve text zones;
- the one chosen music object and at least three explicit source-feature mappings;
- the approved copy and resolved song as context, while reserving all exact text for deterministic typesetting;
- photo preservation invariants and crop/scale-only permissions;
- exact object placement, size, geometry, accent, paper behavior, and hard avoids.

Ask for a blank-paper art base with the conceptual lower-right object, not a finished poster, final typography, client preview, or 4K raster. The top frame is temporary because the finalizer fully replaces it with original pixels. Do not use image generation for text, song, artist, archive, color-accent, progress, or crop-centering corrections.

Call image generation in this turn and return the resulting art-base image so the client can inspect the conceptual object and overall direction. Clearly label it as an intermediate base, not the final poster. Save `art-base.png` and `poster-config.json` to stable absolute paths, record them in the brief, and set `execution.status` to `art_base_ready`.

Stop after showing the art base and say:

`这是音乐物件底图，还不是最终海报。方向没问题的话请回复“继续生成最终预览”；下一轮只做原片回填、正式排版和检查，预计约 2–5 分钟，最终预览会直接作为正文大图展开，并附下载链接。`

Do not run the finalizer or create the quick preview in the art-base turn. This turn boundary keeps the generated base and final poster out of the same media group.

### 8. After Continue, finalize and embed the large preview

Enter this stage only when the brief says `execution.status: art_base_ready` and the client sends “继续生成最终预览” or an unambiguous equivalent. Read the saved paths from the brief. This turn must not call image generation.

Run `scripts/finalize_poster.py` with JSON config to normalize the base, backfill the original photo, typeset the exact approved copy/song/player, and export:

1. a verified 2160×3600 working master;
2. a 1080×1800 client-review PNG via `--out-quick`.

Do not pass `--out-4k` initially. Inspect the review preview at full size and thumbnail size, and run working-master geometry/pixel checks. Treat copy, song, artist, archive, accent, progress, and centering revisions as deterministic config edits; do not regenerate the music object.

After checks pass, update the brief to `execution.status: preview_ready` and record the working-master and quick-preview paths. The review stage is incomplete until `--out-quick` succeeded and the 1080×1800 file exists.

Do not deliver the preview through `view_image`, an image-generation result, a canvas attachment, or a filename alone. In the final response, embed the exact local PNG with standard Markdown image syntax and an absolute path:

```markdown
![最终预览](/absolute/path/to/quick-preview.png)

[下载预览 PNG](/absolute/path/to/quick-preview.png)
```

If the absolute path contains spaces, wrap the Markdown target in angle brackets. Put the inline image before explanatory text so it expands as the primary large image. Include one ordinary download link below it. Do not include any other image or screenshot in this turn.

If the client asks only to fix crop, ratio, sharpness, or source fidelity on an approved poster, run `scripts/backfill_original_photo.py`. Freeze all pixels outside `PHOTO_BOX`, including the entire lower design and sleeve.

### 9. Export 4K only after approval

When the client clearly confirms the visual or asks for 4K/高清, rerun the same approved base and config with `--out-4k`. Do not call image generation again unless they request a creative object change. Verify 3840×6400, 300 DPI, original-photo equality, and concentric geometry.

## Delivery

### Concept confirmation stage

Return the chosen metaphor, three copy options, one recommendation, the song question/range description, and the Sol/Terra/Luna recommendation. State that this confirmation starts art-base generation and that the client will reply Continue once after seeing it. Stop there.

### Review stage

After deterministic finalization completes, place the absolute-path Markdown image at the top of the final response so the preview renders as a large inline image, followed by a clickable download link. Then return the approved proposition, selected song/artist/duration/link when available, one-sentence match reason, and a short source-feature → music-role explanation. End with:

`这是快速预览版，必经步骤已经完成。确认画面后可选导出 4K 终稿，预计约 3–8 分钟；单纯高清导出通常不需要重生成音乐物件，只有修改创意物件时才会再次增加生成额度、时间与 Token。`

After the stage-specific review content, append this creator footer exactly once, as ordinary response text after the image and download link. Do not place it inside the poster image, and do not show it during concept confirmation or art-base review:

```text
如果你玩完这个 Skill 觉得还不错，或者过程中有任何好玩的发现、bug、改进建议，都欢迎来小红书 @鲨鱼小豆（AI版）找我聊聊～

我也特别想看看不同人的旅行照片最后会被翻译成什么。之后应该还会继续做一些新的 Skill ^^
```

### Final stage

After approval, return the 4K path. Keep the handoff concise and do not repeat unchanged explanation. Append the same creator footer exactly once after the 4K link.
