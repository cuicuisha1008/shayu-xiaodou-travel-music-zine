# Approved Brief and Model Handoff

Use this only after the client has confirmed both copy and song. Write `approved-brief.json` in the current task's working directory before offering a model switch.

## Required JSON fields

```json
{
  "schema": "travel-music-zine-approved-brief/v1",
  "locked": true,
  "source_image": "/absolute/path/to/source",
  "source_preflight": {
    "width": 3000,
    "height": 4000,
    "short_edge": 3000,
    "photos_derivative": false,
    "status": "ok",
    "override": false
  },
  "metaphor": "one chosen music metaphor",
  "mappings": [
    {"source_feature": "visible feature", "music_role": "functional role"},
    {"source_feature": "visible feature", "music_role": "functional role"},
    {"source_feature": "visible feature", "music_role": "functional role"}
  ],
  "copy": "client-approved Chinese proposition",
  "song": {
    "source": "client|embedded",
    "title": "exact title",
    "artist": "exact artist",
    "duration": "m:ss or empty for an unverified client track",
    "url": "verified link or empty"
  },
  "visual": {
    "music_object": "specific source-derived object",
    "accent": "photo-derived color description",
    "photo_centering": [0.5, 0.5],
    "sleeve_mode": "restrained"
  },
  "output": {
    "working_master": [2160, 3600],
    "quick_preview": [1080, 1800],
    "four_k_after_approval": [3840, 6400]
  },
  "execution": {
    "status": "approved",
    "art_base_path": "",
    "poster_config_path": "",
    "working_master_path": "",
    "quick_preview_path": ""
  }
}
```

Use only facts already approved or visible in the source. Do not invent an empty field merely to make the JSON look complete.

Populate `source_preflight` from `scripts/preflight_source_image.py`. It describes only the explicitly supplied file. Never populate it by searching a Photos library or guessing that a cached derivative has a corresponding local original. `status: low_resolution_override` is valid only after the client explicitly accepts reduced sharpness.

## Handoff behavior

After saving the file, use the art-base start notice in `model-and-progress-guide.md`, generate and show the art base, then stop for one Continue reply. Any model used after a switch must read this JSON first and treat all locked creative fields as immutable.

Use `execution.status` as a state machine:

1. `approved`: generate and show the art base, record its stable art-base and poster-config paths, set `art_base_ready`, and stop for “继续生成最终预览”.
2. `art_base_ready`: only after Continue, run deterministic finalization without image generation. Record the master and quick-preview paths, set `preview_ready`, and embed the preview using absolute-path Markdown image syntax.
3. `preview_ready`: accept visual review. Deterministic text, song, accent, progress, or crop corrections stay imagegen-free. A requested conceptual-object change returns the state to `approved` and repeats the visible-base review boundary.

Do not re-open the full song library after an embedded match has already been copied into the brief. Do not re-propose copy, re-rank songs, change the metaphor, or reinterpret the mappings unless the client explicitly unlocks them. Never place the art base and final preview in the same assistant turn.
