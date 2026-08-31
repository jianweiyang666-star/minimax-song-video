---
name: minimax-song-video
description: Create original songs with Codex-written lyrics and MiniMax Music, then turn an accepted MP3 and author-provided photos into vertical lyric-video MP4s. Use for story-to-song, reference-song analysis, MiniMax music generation or cover workflows, and photo-matched or photo-derived Remotion lyric videos; not for speech-only TTS or unrelated video editing.
---

# MiniMax Song Video

Turn a story, reference track, voice preference, and photos into reproducible song and lyric-video deliverables. Preserve the user's creative choices while keeping sung lyrics, translations, audio generation, and video rendering as separate artifacts.

## Route the request

Collect whatever the user has already provided; do not ask again for known inputs.

- Story, images, keywords, or emotional direction
- Reference MP3 or a named reference song
- Target sung language and whether translated subtitles are wanted
- Whether to create a new song or revise an accepted melody/voice
- Author photos and output format: MP3, vertical MP4, or both

If a reference MP3 exists, inspect the actual file before describing its style. Summarize only abstract musical attributes; do not copy a released melody, lyrics, or a real singer's identity.

## Required order

1. Inspect the reference audio when supplied.
2. Write a compact style brief: tempo feel, meter, groove, phrasing, energy curve, harmony color, instruments, voice traits, structure, and duration.
3. Draft and review lyrics with Codex before opening MiniMax. Read [references/songwriting.md](references/songwriting.md).
4. Choose MiniMax new-composition or cover mode, prepare the production prompt, generate candidates, and preserve the raw downloads. Read [references/minimax-generation.md](references/minimax-generation.md).
5. Ask the user to choose or accept an audio candidate before spending time on full lyric videos, unless the user explicitly requested all candidates as videos.
6. Build captions from the accepted audio, not from an earlier take. Then design and render the photo-matched MP4. Read [references/lyric-video.md](references/lyric-video.md).
7. Verify audio/video duration, dimensions, codecs, caption timing, and public-facing metadata before delivery.

## Language separation

- The MiniMax lyrics field contains only words that should be sung. Never put translations in it.
- Chinese song: sung lines are Chinese only; prohibit English ad-libs, spoken English, and unintended humming. English subtitle translation is optional and used only when requested.
- English song: sung lines are English only. Prepare a separate Chinese translation track for the lyric video by default.
- Section labels are structural metadata and must not be sung. Keep them distinct from lyric lines.

Use `scripts/validate_caption_pair.py` before rendering bilingual captions. It validates Caption JSON shape, synchronized timing, language separation, and duration bounds.

## Photo-driven backgrounds

- Treat the author's photo as the visual source of truth.
- Use it directly when crop, resolution, and negative space work for 9:16.
- When the photo cannot support a clean vertical layout, Codex may generate or extend a 9:16 background from the photo as a reference. Preserve the recognizable subject, palette, lighting, texture, and location cues; do not invent a different person, place, or story.
- When the user wants the supplied photo refined into a tactile editorial collage, paper-zine, or photo-plus-illustration background, read [references/photo-zine-background.md](references/photo-zine-background.md). Use its scene-card, abstraction, structural-color, and torn-edge workflow while reserving quiet areas for the Remotion title and lyrics.
- Analyze the actual title and lyric regions after cropping. Automatically derive readable primary, translation, inactive, accent, shadow, and scrim colors from the local background rather than using a fixed white-text theme.
- Keep the original photo unchanged and save any generated background as a separate asset.

## Deliverables and provenance

- Keep raw platform downloads separate from share-ready files.
- Do not place “MiniMax generated”, AIGC badges, or platform branding in the public video design.
- When the user wants share-ready files without platform metadata, run `scripts/clean_media_metadata.sh` to create a separate cleaned copy; never destroy the raw source.
- Name variants explicitly so audio, captions, photos, generated backgrounds, and MP4s cannot be mixed between takes.

Stop after two small candidate rounds if the voice, melody, or style is still wrong, and get focused feedback before using more quota.
