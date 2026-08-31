# Photo-driven vertical lyric video

Read this reference after the user has accepted an audio candidate and wants an MP4.

## Inputs

- final cleaned MP3;
- exact sung lyrics;
- subtitle translation only when required;
- one or more author-approved photos;
- title and optional variant label.

Never reuse caption timing from another generation, even when lyrics and melody are similar. Transcribe or align the accepted audio and save captions as Remotion `Caption[]` JSON with `text`, `startMs`, `endMs`, `timestampMs`, and `confidence`.

## Subtitle modes

- Chinese song, Chinese-only video: one Chinese caption track.
- Chinese song, bilingual video requested: Chinese primary plus a separate English translation track.
- English song: English primary plus a separate Chinese translation track by default.

Translations are display-only. Primary and translation arrays must have equal counts and identical start/end times. Run `../scripts/validate_caption_pair.py` before rendering.

## Choose the photo-background mode

Inspect the author's photo before coding. Identify subject location, quiet negative space, dominant light/dark regions, palette, texture, horizon, and safe crop.

1. **Direct photo:** use the original when a 9:16 crop preserves the subject and leaves enough space for title, controls, and lyrics.
2. **Extended photo:** outpaint or extend the supplied photo to 9:16 when the subject is correct but the crop is too tight. Preserve the original center region and extend only the missing canvas.
3. **Photo-derived background:** generate a new background using the supplied photo as visual reference when the user wants a designed scene rather than a literal crop. Preserve the recognizable subject, palette, lighting, texture, location cues, and emotional tone. Do not silently replace a person, landmark, or meaningful object.
4. **Photo-zine background:** when the user wants a paper collage, editorial print, torn-photo, or simplified photo-plus-illustration treatment, read [photo-zine-background.md](photo-zine-background.md). Build the 9:16 background from the source scene rather than applying a generic vintage filter.

Use the image-generation skill for modes 2, 3, or 4. Inspect the supplied image first and save the generated result as a separate asset; never overwrite the author's original. Prefer direct photo mode when it already works.

## Interface and layout

For a music-player feel, use an original playback interface inspired by familiar streaming conventions without copying Spotify, NetEase Cloud Music, or another service's logo or exact chrome. Match the photo through sampled accent colors, paper/film/glass texture, contrast, and corner treatment.

### AI-adaptive lyric typography

Choose lyric colors only after the final 9:16 crop or generated background exists.

1. Inspect or sample the pixels behind the title, active lyric, nearby lyrics, and translation regions. Consider local luminance, color temperature, saturation, texture density, and bright highlights—not only the image-wide average.
2. Derive a stable text theme containing primary lyric, translation, inactive lyric, accent/progress, shadow or outline, and optional local scrim colors.
3. Use light text on reliably dark regions and dark text on reliably light regions. On mixed, detailed, or changing regions, keep the text theme stable and add a subtle localized gradient, blur, outline, or shadow instead of flipping colors line by line.
4. Target at least 4.5:1 contrast for small translations and controls, and at least 3:1 for large active lyrics. If sampled contrast is insufficient, strengthen the local scrim before changing the photo globally.
5. Avoid pure white or pure black when a slightly warm or cool neutral fits the photo better. Derive accents from a visible photo color, then verify that active and inactive states remain distinguishable.
6. Do not let adaptive colors flicker. Use one stable palette for a static photo and only a few gently interpolated palette zones for moving or scene-changing backgrounds.

Render checks must include the lightest, darkest, and most textured lyric-background regions. A visually attractive palette does not pass if any lyric becomes difficult to read.

Default delivery:

- 1080 × 1920, 30 fps, H.264 video plus AAC stereo audio;
- important text at least 80 px from the sides and 100 px from top/bottom;
- title first, playback status second, active lyric third;
- active lyric visually strongest, nearby lines quieter;
- avoid stacking large primary and translated lines too tightly. Give translation a smaller size, looser line height, and at least 8–12 px separation;
- keep public UI free of “MiniMax generated”, AIGC badges, or platform watermarks.

Use Remotion's frame-driven animation APIs. Put media in `public/`, reference it with `staticFile()`, and use `<Audio>` from `@remotion/media`. Load the Remotion create, markup, captions, and render skills before editing or rendering.

## Project layout

Use distinct variant folders:

```text
music-projects/<song>/
  lyrics/<variant>.txt
  candidates/<variant>.raw.mp3
  clean/<variant>.mp3
public/music-projects/<song>/<variant>/
  audio.mp3
  background.original.jpg
  background.vertical.jpg
  lyrics-primary.json
  lyrics-translation.json   # only when needed
  alignment-audit.json
renders/music-projects/<song>/
  <title>-<variant>-vertical.mp4
```

## Verification

1. Render stills at the first sung line, a long lyric, the first chorus, and the final chorus.
2. Check cropping, safe area, line wrapping, active-line contrast, and translation spacing.
3. Render the full MP4 only after stills pass.
4. Use `ffprobe` to verify dimensions, fps, duration, H.264/AAC codecs, and absence of unwanted public metadata.
5. Deliver absolute clickable paths or playable local media embeds.
