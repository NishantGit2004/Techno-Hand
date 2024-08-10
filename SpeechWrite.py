import pyttsx3

class TextToSpeechUtil:
    def __init__(self):
        # Initialize the text-to-speech engine
        self.speech_engine = pyttsx3.init()

    def speak(self, text):
        # Speak the given text
        self.speech_engine.say(text)
        self.speech_engine.runAndWait()
