from datetime import datetime
from PDFGenerator import generate_pdf
from HeaderCollection import collect_header_data, generate_inspection_id
from TireCollection import collect_tire_data
from BatteryCollection import collect_battery_data
from SpeechRead import SpeechRecognizerUtil
from SpeechWrite import TextToSpeechUtil

def main():
    # Initialize utilities and form data
    tts_util = TextToSpeechUtil()
    recognizer_util = SpeechRecognizerUtil()
    form_data = {}

    # Generate Inspection ID
    form_data['Inspection ID'] = generate_inspection_id()

    header_input = recognizer_util.get_speech_input("Do you want to input header data? Say 'yes' to proceed or 'no' to skip.")
    if 'yes' in header_input.lower():
        collect_header_data(tts_util, recognizer_util, form_data)
    else:
        form_data["Header Section"] = "Skipped"

    tire_input = recognizer_util.get_speech_input("Do you want to input tire data? Say 'yes' to proceed or 'no' to skip.")
    if 'yes' in tire_input.lower():
        collect_tire_data(tts_util, recognizer_util, form_data)
    else:
        form_data["Tire Section"] = "Skipped"

    # Add battery data collection
    battery_input = recognizer_util.get_speech_input("Do you want to input battery data? Say 'yes' to proceed or 'no' to skip.")
    if 'yes' in battery_input.lower():
        collect_battery_data(tts_util, recognizer_util, form_data)
    else:
        form_data["Battery Section"] = "Skipped"

    # Generate PDF with the form data
    generate_pdf(form_data)

if __name__ == "__main__":
    main()
