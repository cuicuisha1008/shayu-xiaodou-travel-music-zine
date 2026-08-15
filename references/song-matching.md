# Song Matching

Use this file only when the client has not supplied a song. In that branch, match the photograph to a real song from the bundled `travel-song-library.md` before building the final poster. The local Markdown playlist is the default music source; do not query NetEase or another external service during an ordinary poster run.

If the client supplies an exact song title and artist, do not read this file or `travel-song-library.md`: preserve their metadata and proceed. If they supply only an ambiguous title, ask for the artist instead of silently searching. Use NetEase CLI only when the client explicitly asks for live search, playback, duration lookup, or a playlist refresh.

## 1. Build a Photo Mood Vector

Record these visible axes using short phrases, not invented facts:

- **scene:** coast/waterside / road/travel / rain/wetness / forest/nature / sunset / city lights / night drive / bedroom/interior / abstract;
- **light:** bright, hazy, backlit, golden, overcast, neon, dark;
- **temperature:** cool blue, green, neutral, warm amber, mixed;
- **motion:** still, drifting, walking, flowing, cruising, rushing;
- **space:** enclosed, framed, layered, open, panoramic;
- **social energy:** empty, solitary, intimate pair, small group, crowd;
- **emotion:** weightless, playful, tender, distant, nostalgic, restless, nocturnal;
- **music energy:** R&B, Neo-Soul, relaxed vocals, indie pop/rock, psychedelic, acoustic, orchestral, dance/electronic, Latin-leaning.

## 2. Rank the Personal Library

Read the full table. Filter by comment-derived atmosphere and scene first, then score plausible candidates out of 100:

- scene and atmosphere fit: 30;
- emotional temperature: 25;
- motion and energy: 15;
- light/color resonance: 10;
- social relation and intimacy: 10;
- comment-signal confidence: 5;
- series freshness: 5.

Prefer high-confidence atmosphere rows when they fit, but never let confidence override a poor scene match. Treat `抽象听感` rows cautiously because their comments contain little scene evidence. Keep three private finalists and choose one; expose alternatives only if the user asks.

Do not choose by song title alone. A track named after a city, flower, color, season, road, or ocean is not automatically a match. Do not infer lyrical meaning unless lyrics were actually inspected.

## 3. User-Specified Songs

If the user names a song, it overrides automatic selection. Preserve the supplied spelling, artist, and deliberate casing such as `seasons`. Do not invent or fetch a duration unless the user explicitly asks.

## 4. Embedded-library authority and CLI boundary

For clients without a special music request, the bundled library is authoritative. Read and rank it locally, use the exact title, artist, and verified duration printed in its table, and extract the plain numeric NetEase song ID from its existing Markdown link. Do not invoke CLI merely to confirm the same song, obtain a fresher comment count, or refill the player's duration.

Every bundled row contains a verified `m:ss` duration. Render it on the player's right endpoint. If a malformed row lacks duration, reject that match and choose another complete row rather than delivering a visibly incomplete player.

Use `netease-music-cli` only when the user explicitly asks for one of these actions:

- search or select music outside the bundled 100 songs;
- play or control music;
- obtain an exact missing duration;
- refresh, replace, or expand the bundled playlist.

Then follow the NetEase CLI Skill exactly. Never run CLI silently as a routine poster-generation step.

## 5. Poster Field

Render in the lower-left zone:

1. Chinese proposition;
2. track title;
3. artist;
4. small play triangle and thin progress line;
5. `00:00` at left and the bundled verified `m:ss` duration at right; for a client-supplied track, add the right duration only when they supplied or explicitly verified it;
6. optional `TRAVEL ARCHIVE` in microtype.

Track information stays subordinate to the proposition and music object. It should feel like an album-booklet annotation, not a streaming-app screenshot.

## 6. Series Discipline

For several posters, keep a used-track list in the working notes. Avoid adjacent repetition in:

- track;
- artist;
- atmosphere family;
- music-object grammar.

When a set contains varied photographs, sequence contrasting atmosphere families—coast, night, rain, nature, interior, city, romantic, or dreamlike—instead of maximizing each image independently.
