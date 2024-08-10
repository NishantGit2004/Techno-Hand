from SpeechRead import SpeechRecognizerUtil
from SpeechWrite import TextToSpeechUtil

def collect_battery_data(tts_util, recognizer_util, form_data):
    # Collect Battery Make
    form_data["Battery Make"] = recognizer_util.get_speech_input("Please say the battery make (e.g., CAT, ABC, XYZ).")

    # Collect Battery Replacement Date
    form_data["Battery Replacement Date"] = recognizer_util.get_speech_input("Please say the battery replacement date.")

    # Collect Battery Voltage
    # form_data["Battery Voltage"] = recognizer_util.get_speech_input("Please say the battery voltage (e.g., 12V, 13V).")

    # # Collect Battery Water Level
    # form_data["Battery Water Level"] = recognizer_util.get_speech_input("Please say the battery water level (Good, Ok, Low).")

    # # Collect Condition of Battery
    # form_data["Battery Condition"] = recognizer_util.get_speech_input("Is there any damage to the battery? Say 'yes' or 'no'.")
    
    # # Collect Information on Leak/Rust
    # form_data["Battery Leak/Rust"] = recognizer_util.get_speech_input("Is there any leak or rust in the battery? Say 'yes' or 'no'.")

    # # Collect Battery Overall Summary
    # form_data["Battery Overall Summary"] = recognizer_util.get_speech_input("Please provide an overall battery summary (up to 1000 characters).")

