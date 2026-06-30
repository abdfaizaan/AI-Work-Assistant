"""Console workflow for recording audio with AudioRecorder."""

from __future__ import annotations

import os
from pathlib import Path

from record import AudioRecorder


def main() -> None:
    """Run the recording workflow from the command line."""
    recordings_dir = Path(__file__).resolve().parent.parent / "recordings"
    recordings_dir.mkdir(parents=True, exist_ok=True)

    recorder = AudioRecorder()

    input("Press ENTER to start recording...")
    print("Recording... Press ENTER to stop.")
    recorder.start()

    input()
    audio_data = recorder.stop()

    output_path = recordings_dir / "recording.wav"
    recorder.save(str(output_path))

    print(f"Saved recording to: {output_path}")
    print(f"Captured {audio_data.shape[0]} frames at {recorder.samplerate} Hz.")


if __name__ == "__main__":
    main()
