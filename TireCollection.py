from SpeechRead import SpeechRecognizerUtil
from SpeechWrite import TextToSpeechUtil

def collect_tire_data(tts_util, recognizer_util, form_data):
    tire_positions = ["Left Front", "Right Front", "Left Rear", "Right Rear"]
    for position in tire_positions:
        form_data[f"Tire Pressure for {position}"] = recognizer_util.get_speech_input(f"Please say the tire pressure for {position}.")
        form_data[f"Tire Condition for {position}"] = recognizer_util.get_speech_input(f"Please say the tire condition for {position} (Good, Ok, Needs Replacement).")

    form_data["Overall Tire Summary"] = recognizer_util.get_speech_input("Please provide an overall tire summary.")
