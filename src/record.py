"""Audio recording helper using scipy.io.wavfile for saving WAV files."""

from __future__ import annotations

import threading
from typing import Optional

import numpy as np
import sounddevice as sd
from scipy.io import wavfile


class AudioRecorder:
    """A modular audio recorder with start/stop/save functionality."""

    def __init__(
        self,
        samplerate: int = 44100,
        channels: int = 1,
        dtype: str = "int16",
    ) -> None:
        """Initialize recorder settings without starting audio capture."""
        self.samplerate = samplerate
        self.channels = channels
        self.dtype = dtype
        self._buffer: list[np.ndarray] = []
        self._stream: Optional[sd.InputStream] = None
        self._lock = threading.Lock()
        self.audio_data: Optional[np.ndarray] = None

    def _callback(self, indata: np.ndarray, frames: int, time, status) -> None:
        """Receive audio frames from the input stream and store them in a buffer."""
        if status:
            # Keep recording even if there are status warnings.
            return

        with self._lock:
            self._buffer.append(indata.copy())

    def start(self) -> None:
        """Start recording audio asynchronously using an InputStream."""
        with self._lock:
            if self._stream is not None:
                raise RuntimeError("AudioRecorder is already recording.")

            self._buffer = []
            self.audio_data = None
            self._stream = sd.InputStream(
                samplerate=self.samplerate,
                channels=self.channels,
                dtype=self.dtype,
                callback=self._callback,
            )
            self._stream.start()

    def stop(self) -> np.ndarray:
        """Stop recording and return the captured audio frames as a NumPy array."""
        with self._lock:
            if self._stream is None:
                raise RuntimeError("AudioRecorder is not recording.")

            self._stream.stop()
            self._stream.close()
            self._stream = None

            if self._buffer:
                self.audio_data = np.concatenate(self._buffer, axis=0)
            else:
                self.audio_data = np.empty((0, self.channels), dtype=self.dtype)

            self._buffer = []

        return self.audio_data

    def save(self, filename: str) -> None:
        """Save the most recent recording to a WAV file using scipy.io.wavfile."""
        if self.audio_data is None:
            raise RuntimeError("No audio data available. Call start() and stop() first.")

        wavfile.write(filename, self.samplerate, self.audio_data)
