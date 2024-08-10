from datetime import datetime
from SpeechRead import SpeechRecognizerUtil
from SpeechWrite import TextToSpeechUtil

# Define the generate_inspection_id function here
def generate_inspection_id():
    generate_inspection_id.counter += 1
    return generate_inspection_id.counter

generate_inspection_id.counter = 0

def collect_header_data(tts_util, recognizer_util, form_data):
    form_data["Truck Serial Number"] = recognizer_util.get_speech_input("Please say the truck serial number.")
    form_data["Truck Model"] = recognizer_util.get_speech_input("Please say the truck model.")
    form_data["Inspection ID"] = generate_inspection_id()  # Use the local generate_inspection_id
    # form_data["Inspector Name"] = recognizer_util.get_speech_input("Please say your name.")
    # form_data["Inspection Employee ID"] = recognizer_util.get_speech_input("Please say your employee ID.")
    # form_data["Date & Time of Inspection"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # form_data["Location of Inspection"] = recognizer_util.get_speech_input("Please say the location of inspection.")
    # form_data["Geo Coordinates of Inspection"] = recognizer_util.get_speech_input("Please say the geo coordinates of inspection (or skip if not applicable).")
    # form_data["Service Meter Hours"] = recognizer_util.get_speech_input("Please say the service meter hours (odometer reading).")
    # form_data["Inspector Signature"] = recognizer_util.get_speech_input("Please say your signature to confirm the inspection.")
    # form_data["Customer Name/Company Name"] = recognizer_util.get_speech_input("Please say the customer or company name.")
    # form_data["CAT Customer ID"] = recognizer_util.get_speech_input("Please say the CAT customer ID.")
