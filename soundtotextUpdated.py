from pathlib import Path
from faster_whisper import WhisperModel

# Remember to change the path!
INPUT_FOLDER = Path(r"D:\1 Archived Projects\Waze F1 VO\Game Audio Files\F1 2020\EN\en_re_startup")
OUTPUT_FILE = "transcriptions.txt"

model = WhisperModel(
    "large-v3-turbo",
    device="cuda",          # Change to "cpu" if no gpu, requires cuda 12 specifically
    compute_type="float32"
)

# Find all .ogg files (case-insensitive)
audio_files = [
    f for f in INPUT_FOLDER.iterdir()
    if f.is_file() and f.suffix.lower() == ".ogg"
]

total = len(audio_files)
print(f"Found {total} audio files.\n")

with open(OUTPUT_FILE, "w", encoding="utf-8") as output:

    for i, audio_file in enumerate(sorted(audio_files), start=1):

        print(f"[{i}/{total}] Processing {audio_file.name}...")

        segments, info = model.transcribe(
            str(audio_file),
            language="en",
            beam_size=8,
            best_of=8,
            temperature=0,
            vad_filter=True,
            condition_on_previous_text=False
        )

        text = " ".join(segment.text.strip() for segment in segments)

        if text:
            print(f"    ✓ {text}")
            output.write(f"{audio_file.name}: {text}\n")
        else:
            print("    ✗ No speech detected")
            output.write(f"{audio_file.name}: [No speech detected]\n")

print("\nDone!")