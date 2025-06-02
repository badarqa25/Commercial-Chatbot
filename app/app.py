from flask import Flask, render_template, request, jsonify
import json
import os

# Create Flask app instance (this must be named 'app' for Gunicorn)
app = Flask(__name__)

# Load predefined responses
def load_responses():
    with open(os.path.join(os.path.dirname(__file__), 'responses.json'), 'r') as f:
        return json.load(f)

responses = load_responses()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['message'].lower()
    
    # Check for exact matches first
    for intent in responses['intents']:
        if user_message in intent['patterns']:
            return jsonify({'response': intent['responses'][0]})
    
    # Check for partial matches
    for intent in responses['intents']:
        for pattern in intent['patterns']:
            if pattern in user_message:
                return jsonify({'response': intent['responses'][0]})
    
    # Default response if no match found
    return jsonify({'response': responses['default_response']})

# This block is crucial for Gunicorn
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
