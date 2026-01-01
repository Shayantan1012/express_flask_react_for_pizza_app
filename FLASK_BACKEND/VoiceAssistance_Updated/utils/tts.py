import pyttsx3
import threading

_engine_lock = threading.Lock()


def speak(text: str) -> None:
    """
    Speak text synchronously.
    Reinitializes engine each time to avoid silent failures.
    """
    if not text:
        return

    with _engine_lock:
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[1].id)
        engine.setProperty("rate", 175)
        engine.setProperty("volume", 1.0)

        engine.say(text)
        engine.runAndWait()

        engine.stop()
