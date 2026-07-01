"""Console workflow for recording audio with AudioRecorder."""

from __future__ import annotations

import logging
from pathlib import Path

from record import AudioRecorder
import sounddevice as sd


def main() -> None:
    """Run the recording workflow from the command line."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s",
    )
    logger = logging.getLogger(__name__)

    recordings_dir = Path(__file__).resolve().parent.parent / "recordings"
    recordings_dir.mkdir(parents=True, exist_ok=True)

    recorder = AudioRecorder()

    try:
        input("Press ENTER to start recording...")
        print("Recording... Press ENTER to stop.")
        recorder.start()

        input()
        audio_data = recorder.stop()

        output_path = recordings_dir / "recording.wav"
        recorder.save(str(output_path))

        print(f"Saved recording to: {output_path}")
        print(f"Captured {audio_data.shape[0]} frames at {recorder.samplerate} Hz.")
        logger.info("Recording saved successfully to %s", output_path)

    except sd.PortAudioError as error:
        logger.error("Microphone unavailable or audio device failed to open.")
        logger.debug("PortAudio error details: %s", error, exc_info=True)
        print("Error: Unable to access the microphone. Please verify your audio input device and try again.")

    except Exception as error:
        logger.exception("Unexpected error in the recording workflow.")
        print("An unexpected error occurred. Please check the logs for more details.")


if __name__ == "__main__":
    main()
