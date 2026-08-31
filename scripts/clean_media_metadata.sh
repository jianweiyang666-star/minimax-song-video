#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 INPUT OUTPUT" >&2
  exit 2
fi

input=$1
output=$2

if [[ ! -f "$input" ]]; then
  echo "Input does not exist: $input" >&2
  exit 2
fi

if [[ -e "$output" ]]; then
  echo "Output already exists; refusing to overwrite: $output" >&2
  exit 2
fi

if command -v ffmpeg >/dev/null 2>&1; then
  ffmpeg_bin=$(command -v ffmpeg)
elif [[ -x node_modules/@remotion/compositor-darwin-arm64/ffmpeg ]]; then
  ffmpeg_bin=node_modules/@remotion/compositor-darwin-arm64/ffmpeg
  export DYLD_LIBRARY_PATH=node_modules/@remotion/compositor-darwin-arm64
else
  echo "ffmpeg was not found in PATH or the current Remotion project" >&2
  exit 2
fi

"$ffmpeg_bin" -hide_banner -loglevel error -n -i "$input" \
  -map_metadata -1 -c copy "$output"

echo "$output"
