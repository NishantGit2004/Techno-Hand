from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from PDFGenerator import generate_pdf
from HeaderCollection import collect_header_data, generate_inspection_id
from TireCollection import collect_tire_data
from BatteryCollection import collect_battery_data
from SpeechRead import SpeechRecognizerUtil
from SpeechWrite import TextToSpeechUtil

app = Flask(__name__)
tts_util = TextToSpeechUtil()
recognizer_util = SpeechRecognizerUtil()

# Initialize MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["inspectionDB"]

# Define collections
header_collection = db["header"]
tires_collection = db["tires"]
battery_collection = db["battery"]
exterior_collection = db["exterior"]
brakes_collection = db["brakes"]
engine_collection = db["engine"]
voc_collection = db["voice_of_customer"]

# Create or Update Header Data
@app.route('/header', methods=['GET'])
def add_header():
    headerData = {}
    data = collect_header_data(tts_util, recognizer_util, headerData)
    result = header_collection.insert_one(data)
    return jsonify({"message": "Header data added", "id": str(result.inserted_id)}), 201

# Retrieve Header Data
@app.route('/header/<header_id>', methods=['GET'])
def get_header(header_id):
    header = header_collection.find_one({"_id": header_id})
    if header:
        return jsonify(header), 200
    return jsonify({"error": "Header not found"}), 404

# Retrieve All Header Data
@app.route('/headers', methods=['GET'])
def get_all_headers():
    headers = list(header_collection.find())
    for header in headers:
        header['_id'] = str(header['_id'])  # Convert ObjectId to string
    return jsonify(headers), 200

# Create or Update Tire Data
@app.route('/tires', methods=['POST'])
def add_tires():
    data = request.json
    result = tires_collection.insert_one(data)
    return jsonify({"message": "Tire data added", "id": str(result.inserted_id)}), 201

# Retrieve Tire Data
@app.route('/tires/<tire_id>', methods=['GET'])
def get_tires(tire_id):
    tires = tires_collection.find_one({"_id": tire_id})
    if tires:
        return jsonify(tires), 200
    return jsonify({"error": "Tire data not found"}), 404

# Retrieve All Tire Data
@app.route('/tires', methods=['GET'])
def get_all_tires():
    tires = list(tires_collection.find())
    for tire in tires:
        tire['_id'] = str(tire['_id'])  # Convert ObjectId to string
    return jsonify(tires), 200

# Create or Update Battery Data
@app.route('/battery', methods=['POST'])
def add_battery():
    data = request.json
    result = battery_collection.insert_one(data)
    return jsonify({"message": "Battery data added", "id": str(result.inserted_id)}), 201

# Retrieve Battery Data
@app.route('/battery/<battery_id>', methods=['GET'])
def get_battery(battery_id):
    battery = battery_collection.find_one({"_id": battery_id})
    if battery:
        return jsonify(battery), 200
    return jsonify({"error": "Battery data not found"}), 404

# Retrieve All Battery Data
@app.route('/batteries', methods=['GET'])
def get_all_batteries():
    batteries = list(battery_collection.find())
    for battery in batteries:
        battery['_id'] = str(battery['_id'])  # Convert ObjectId to string
    return jsonify(batteries), 200

# Create or Update Exterior Data
@app.route('/exterior', methods=['POST'])
def add_exterior():
    data = request.json
    result = exterior_collection.insert_one(data)
    return jsonify({"message": "Exterior data added", "id": str(result.inserted_id)}), 201

# Retrieve Exterior Data
@app.route('/exterior/<exterior_id>', methods=['GET'])
def get_exterior(exterior_id):
    exterior = exterior_collection.find_one({"_id": exterior_id})
    if exterior:
        return jsonify(exterior), 200
    return jsonify({"error": "Exterior data not found"}), 404

# Retrieve All Exterior Data
@app.route('/exteriors', methods=['GET'])
def get_all_exteriors():
    exteriors = list(exterior_collection.find())
    for exterior in exteriors:
        exterior['_id'] = str(exterior['_id'])  # Convert ObjectId to string
    return jsonify(exteriors), 200

# Create or Update Brakes Data
@app.route('/brakes', methods=['POST'])
def add_brakes():
    data = request.json
    result = brakes_collection.insert_one(data)
    return jsonify({"message": "Brakes data added", "id": str(result.inserted_id)}), 201

# Retrieve Brakes Data
@app.route('/brakes/<brakes_id>', methods=['GET'])
def get_brakes(brakes_id):
    brakes = brakes_collection.find_one({"_id": brakes_id})
    if brakes:
        return jsonify(brakes), 200
    return jsonify({"error": "Brakes data not found"}), 404

# Retrieve All Brakes Data
@app.route('/brakes', methods=['GET'])
def get_all_brakes():
    brakes = list(brakes_collection.find())
    for brake in brakes:
        brake['_id'] = str(brake['_id'])  # Convert ObjectId to string
    return jsonify(brakes), 200

# Create or Update Engine Data
@app.route('/engine', methods=['POST'])
def add_engine():
    data = request.json
    result = engine_collection.insert_one(data)
    return jsonify({"message": "Engine data added", "id": str(result.inserted_id)}), 201

# Retrieve Engine Data
@app.route('/engine/<engine_id>', methods=['GET'])
def get_engine(engine_id):
    engine = engine_collection.find_one({"_id": engine_id})
    if engine:
        return jsonify(engine), 200
    return jsonify({"error": "Engine data not found"}), 404

# Retrieve All Engine Data
@app.route('/engines', methods=['GET'])
def get_all_engines():
    engines = list(engine_collection.find())
    for engine in engines:
        engine['_id'] = str(engine['_id'])  # Convert ObjectId to string
    return jsonify(engines), 200

# Create or Update Voice of Customer Data
@app.route('/voice_of_customer', methods=['POST'])
def add_voc():
    data = request.json
    result = voc_collection.insert_one(data)
    return jsonify({"message": "Voice of Customer data added", "id": str(result.inserted_id)}), 201

# Retrieve Voice of Customer Data
@app.route('/voice_of_customer/<voc_id>', methods=['GET'])
def get_voc(voc_id):
    voc = voc_collection.find_one({"_id": voc_id})
    if voc:
        return jsonify(voc), 200
    return jsonify({"error": "Voice of Customer data not found"}), 404

# Retrieve All Voice of Customer Data
@app.route('/voice_of_customers', methods=['GET'])
def get_all_voc():
    vocs = list(voc_collection.find())
    for voc in vocs:
        voc['_id'] = str(voc['_id'])  # Convert ObjectId to string
    return jsonify(vocs), 200

if __name__ == "__main__":
    app.run(debug=True)
