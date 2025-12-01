import speech_recognition as sr
import pyttsx3
import threading
import os
import tempfile
from groq import Groq
from . import config

class VoiceEngine:
    def __init__(self):
        try:
            self.engine = pyttsx3.init()
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
            self.groq_client = Groq(api_key=config.GROQ_API_KEY)
        except Exception as e:
            print(f"Voice Engine Init Error: {e}")
            self.engine = None
            self.groq_client = None

    def speak(self, text):
        """
        Speaks the text using TTS.
        Runs in a separate thread to avoid blocking the UI.
        """
        if not self.engine:
            return

        def _speak():
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception as e:
                print(f"TTS Error: {e}")

        threading.Thread(target=_speak).start()

    def listen(self, timeout=5):
        """
        Listens for audio input and returns the recognized text using Groq (Whisper).
        """
        if not self.engine: # Check if init failed (e.g. no mic)
             return None

        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                # Listen
                audio = self.recognizer.listen(source, timeout=timeout)
            
            # Save to temp file for Groq API
            
            # Save to temp file for Groq API
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
                tmp_file.write(audio.get_wav_data())
                tmp_filename = tmp_file.name

            # Send to Groq Whisper
            try:
                with open(tmp_filename, "rb") as file:
                    transcription = self.groq_client.audio.transcriptions.create(
                        file=(tmp_filename, file.read()),
                        model="distil-whisper-large-v3-en",
                        response_format="json",
                        language="en",
                        temperature=0.0
                    )
                text = transcription.text.strip()
            except Exception as e:
                print(f"Groq STT Error: {e}")
                text = None
            finally:
                # Cleanup temp file
                if os.path.exists(tmp_filename):
                    os.remove(tmp_filename)

            print(f"Heard: {text}")
            return text

        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return None
        except Exception as e:
            print(f"STT Error: {e}")
            return None
