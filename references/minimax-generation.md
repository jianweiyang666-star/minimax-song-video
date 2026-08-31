# MiniMax Music generation

Read this reference when generating or revising music at the domestic MiniMax Music page.

## Access

Use the domestic page: `https://www.minimaxi.com/audio/music`.

Do not assume a stable public API or installed connector. Prefer an available MiniMax connector if one exists; otherwise use the Chrome or in-app browser skill with the user's existing signed-in session. Never request, expose, or copy the user's password or session tokens.

## Choose the generation mode

### New composition

Use when the user has a story, lyrics, photos, or an abstract style brief but no accepted melody. The prompt may use reference analysis, but must request original melody, chords, and arrangement.

### Cover or revision

Use when the user wants to keep an accepted song's melody, timing, structure, or singer feel while changing lyrics. Start the cover action from the accepted result card or upload that accepted MP3 as reference.

MiniMax cover mode can preserve musical structure but does not guarantee identical vocal identity. Say this clearly. To improve consistency, describe the accepted voice through register, brightness, breath, nasality, diction, microphone distance, reverb, and emotional intensity; generate a small number of candidates and let the user compare.

## Prompt structure

Keep the lyrics and production prompt in separate fields.

Production prompt order:

1. original composition or reference-preservation instruction;
2. genre, tempo feel or BPM, meter, and groove;
3. melodic phrase length, rests, hook behavior, and energy curve;
4. vocal register, timbre traits, diction, language, and performance restraint;
5. core instruments, arrangement by section, and mix space;
6. structural and duration target;
7. negative constraints;
8. lyric-integrity instruction: sing every lyric line in order, including repeated choruses.

Avoid prompt contradictions such as “very slow” plus “dense continuous sixteenth notes.” If tempo has double-time texture, state which layer controls the singer's breathing.

## Candidate workflow

1. Fill the reviewed sung lyrics.
2. Fill the style/production prompt.
3. Give the candidate a unique title containing variant and revision.
4. Generate one or two candidates per round.
5. Check language, skipped lines, structure, tempo feel, voice, and duration before downloading.
6. Download `MP3(无水印)` and keep it as a raw candidate.
7. Record the source/reference, prompt, title, and duration next to the candidate.
8. Produce a cleaned share copy only when requested. Use `../scripts/clean_media_metadata.sh` and retain the raw file.

If local upload is blocked in Chrome, the user may need to enable file-URL access for the browser extension. Prefer reusing a saved MiniMax result card as the cover source when that avoids a needless upload.

## Stopping condition

After two small rounds, stop and ask what is wrong in concrete terms: voice brightness, tempo feel, vocal phrasing, hook, arrangement, or lyric fit. Do not burn quota on repeated blind retries.
