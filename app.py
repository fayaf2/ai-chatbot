from flask import Flask, render_template, jsonify
import requests
import json

app = Flask(__name__)


# Function to generate content using the Gemini API
def generate_content(api_key, text_input):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        "contents": [{
            "parts": [{"text": text_input}]
        }]
    }

    # Make the API request
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        generated_content = response_data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get(
            "text", "No content generated")

        # Split the generated content into sentences and return the first sentence
        sentences = generated_content.split('.')
        first_sentence = sentences[0].strip() + '.' if sentences else "No content generated."
        return first_sentence
    else:
        return "Error in generating content."


# Route to serve index.html
@app.route('/')

def index():
    return render_template('s.html')


# API route for generating content from speech
@app.route('/generate_content/<text>', methods=['GET'])
def generate_content_api(text):
    # Set your Gemini API key here
    api_key = 'Paste Your API Key'
    content = generate_content(api_key, text)
    return jsonify({'content': content})


# Start the app with Gunicorn or Flask's built-in server for testing
if __name__ == "__main__":
    app.run(debug=True)
