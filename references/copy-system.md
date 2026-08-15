# Copy Confirmation System

Use this short stage after choosing one source-specific music metaphor and before reading design resources or calling image generation.

## Produce three options

All three options must express the same chosen metaphor, not three unrelated concepts:

1. **Concrete/source-specific:** names the visible relationship most clearly.
2. **Poetic/album-title:** has one imaginative turn and reads like a memorable record title.
3. **Restrained/editorial:** quieter and more spacious, with minimal explanation.

Each option should normally be 12–28 Chinese characters. Use one meaningful music verb or structure such as `录进`, `刻进`, `混成`, `采样`, `循环`, `转调`, `左右声道`, `B 面`, or `回声`. Never invent a place, date, weather, BPM, lyric meaning, or track fact. Recommend one option and say why in one short phrase.

## Ask about the song in the same message

Ask whether the client already has a song they want to place. If yes, request the exact title and artist and do not load the bundled song-matching resources. If no, say that one track will be matched automatically from the Skill's embedded 100-song travel-atmosphere library.

Describe the current library concisely and accurately:

- 100 lesser-known tracks added to the owner's favorites from 2025 onward, all below 10,000 NetEase comments;
- main sound: R&B, Neo-Soul, relaxed vocals, indie pop/rock, romantic night-drive moods, coastal/waterside light, rain, forest/nature, bedroom intimacy, and dreamlike city scenes;
- language range: 94 English/mixed-language tracks, 3 Korean tracks, and 3 Spanish/mixed-language tracks;
- every row contains a verified `m:ss` duration, so a matched built-in track can render a complete player.

## Client-facing template

> 我把这张理解为「{metaphor}」：{three short source-feature → music-role mappings}。我会直接采用这个意象。
>
> 文案给你三个版本：
> 1. {concrete}
> 2. {poetic}
> 3. {restrained}
>
> 我推荐第 {n} 个，{short reason}。
>
> 另外，你有想放的歌曲吗？有的话请发“歌名 + 歌手”；没有的话，我会从内置 100 首旅行氛围曲里自动匹配。曲库以近年收藏的小众 R&B、Neo-Soul、松弛人声和独立流行/摇滚为主，覆盖海岸、水边、夜行、雨天、森林、卧室与梦感城市等氛围；94 首为英语/跨语种，另有少量韩语与西语歌曲，全部带准确时长。
>
> 请选择文案，并告诉我是否有指定歌曲。收到回复后我会先生成并展示音乐物件底图；你确认方向后再回复一次“继续生成最终预览”，下一轮会完成原片回填、正式排版和检查，并把最终预览直接作为正文大图展开。看到预览后，是否导出 4K 由你决定。
>
> 模型建议：5.6 Sol 的意象理解和质感最好，但耗时与 Token 相对最高；5.6 Terra 速度更快，通常能达到约 70%–80% 的效果；Luna 的意象与质感实测明显较弱，不建议用于正式出图。如果想用 Terra，请在发送这次确认回复前切换；确认一发出，底图生成就会开始。

Stop after this message and wait for the client's copy choice and song decision. Do not inspect the layout master, read the full song library, call image generation, create an approval brief, or create a preview yet. Do not tell the client to switch models before both copy and song are resolved. If the client explicitly says “直接做”“不用确认” or equivalent, use the recommended copy and continue; still honor any supplied song. Read `model-and-progress-guide.md` before composing any altered checkpoint wording.
