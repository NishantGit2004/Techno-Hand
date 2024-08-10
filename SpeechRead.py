import speech_recognition as sr
from SpeechWrite import TextToSpeechUtil

class SpeechRecognizerUtil:
    def __init__(self):
        # Initialize the recognizer
        self.recognizer = sr.Recognizer()

    def get_speech_input(self, prompt):
        tts_util = TextToSpeechUtil()
        
        # Speak the prompt to the user once
        print(prompt)
        tts_util.speak(prompt)
        
        while True:
            with sr.Microphone() as source:
                # Adjust the recognizer sensitivity to ambient noise
                self.recognizer.adjust_for_ambient_noise(source)
                # Listen to the user input
                audio = self.recognizer.listen(source)

                try:
                    # Convert speech to text
                    text = self.recognizer.recognize_google(audio)
                    print(f"You said: {text}")
                    return text
                except sr.UnknownValueError:
                    # Prompt for repeat without repeating the original question
                    tts_util.speak("Could you please repeat?")
                except sr.RequestError:
                    print("Sorry, the service is down.")
                    return None
