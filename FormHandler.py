from flask import Flask, render_template, request
from HeaderCollection import collect_header_data, generate_inspection_id
from TireCollection import collect_tire_data
from PDFGenerator import generate_pdf
from SpeechRead import SpeechRecognizerUtil
from SpeechWrite import TextToSpeechUtil

def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            # Get the form data from the POST request
            form_data = request.form.to_dict()

            # Ensure 'Inspection ID' is present
            if 'Inspection ID' not in form_data:
                form_data['Inspection ID'] = generate_inspection_id()

            # Generate PDF with the form data
            generate_pdf(form_data)

            return "Form submitted successfully! PDF generated."

        else:
            # Initialize utilities and form data
            tts_util = TextToSpeechUtil()
            recognizer_util = SpeechRecognizerUtil()
            form_data = {}

            # Generate Inspection ID
            form_data['Inspection ID'] = generate_inspection_id()

            # Ask if user wants to input header data
            tts_util.speak("Do you want to input header data? Say 'yes' to proceed or 'no' to skip.")
            header_input = recognizer_util.get_speech_input("Do you want to input header data? Say 'yes' to proceed or 'no' to skip.")
            if 'yes' in header_input.lower():
                collect_header_data(tts_util, recognizer_util, form_data)
            else:
                form_data["Header Section"] = "Skipped"

            # Ask if user wants to input tire data
            tts_util.speak("Do you want to input tire data? Say 'yes' to proceed or 'no' to skip.")
            tire_input = recognizer_util.get_speech_input("Do you want to input tire data? Say 'yes' to proceed or 'no' to skip.")
            if 'yes' in tire_input.lower():
                collect_tire_data(tts_util, recognizer_util, form_data)
            else:
                form_data["Tire Section"] = "Skipped"

            # Render form with collected data as default values
            return render_template("form.html", form_data=form_data)

    return app
