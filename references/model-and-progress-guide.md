# Model and Progress Guide

Use these client-facing estimates as planning ranges, not guarantees. Queue load, source complexity, retries, and local export speed can change them. Never invent an exact Token count because the interface does not expose a reliable per-poster forecast.

## Model recommendation

- **5.6 Sol — recommended:** strongest source reading, metaphor, composition judgment, and paper/object material quality. Expect high relative reasoning/Token use. Concept confirmation usually takes `2–5 min`; the art-base generation turn usually takes `8–20 min`.
- **5.6 Terra — acceptable faster option:** usually retains roughly `70%–80%` of the Sol result for this Skill. Expect medium relative reasoning/Token use. Concept confirmation usually takes `1–3 min`; the art-base generation turn usually takes `5–12 min`.
- **5.6 Luna — not recommended:** usually faster with lower relative consumption, but real tests showed materially weaker metaphor extraction, object construction, and texture. Retries can erase the apparent saving. Mention it only to advise against it; never present it as the default handoff.

Deterministic finalization after the art base usually takes `2–5 min` on any model. Optional 4K export and verification usually take `3–8 min`.

Approximate active work from first photo analysis through quick preview is `12–30 min` with Sol and `8–20 min` with Terra, excluding the client's copy/song reply, the later Continue reply, and any retry. These totals are planning ranges, not completion promises.

## Checkpoint 0 — beginning photo analysis

Before inspecting or reading references, send a short non-blocking update and continue working:

> 我先分析照片，并给你一个明确意象、3 版文案和歌曲选择。这一步用 5.6 Sol 通常约 2–5 分钟；用 Terra 通常约 1–3 分钟。整套快速预览若不返工，Sol 的实际处理时间约 12–30 分钟，Terra 约 8–20 分钟。确认文案和歌曲后我会先展示音乐物件底图；你看过后只需回复一次“继续”，下一轮会直接展开最终预览大图。

## Checkpoint 1 — concept, copy, and song

End the first proposal with:

> 请选择文案，并告诉我是否有指定歌曲。收到回复后我会先生成并展示音乐物件底图；你确认方向后再回复一次“继续生成最终预览”，下一轮会完成原片回填、正式排版和检查，并把最终预览直接作为正文大图展开。看到预览后，是否导出 4K 由你决定。
>
> 模型建议：5.6 Sol 的意象理解和质感最好，但耗时与 Token 相对最高；5.6 Terra 速度更快，通常能达到约 70%–80% 的效果；Luna 的意象与质感实测明显较弱，不建议用于正式出图。如果想用 Terra，请在发送这次确认回复前切换；确认一发出，底图生成就会开始。

## Art-base generation after confirmation

After saving `approved-brief.json`, send this non-blocking update and continue generating the visible art base:

> 文案和歌曲已经锁定，现在开始生成音乐物件底图。使用 5.6 Sol 通常约 8–20 分钟；使用 Terra 通常约 5–12 分钟。底图会先展示给你；确认方向后回复一次“继续生成最终预览”，正式排版与检查约需 2–5 分钟。

After showing the art base, stop and request “继续生成最终预览”. When the client continues, announce the `2–5 min` finalization range. Deliver the completed preview as an absolute-path Markdown image, not as a tool attachment, then describe 4K as optional.

## Token wording

Use only `高 / 中等 / 较低` or comparative wording. Do not quote a numeric Token total or claim a percentage of Token savings. The `70%–80%` figure describes expected visual outcome, not Token use.
