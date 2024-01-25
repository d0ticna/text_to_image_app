import os
from openai import OpenAI
from flask import Flask, request, jsonify,render_template
import logging
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
CORS(app)
#
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#Retrieve API key from environment variable
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])


@app.route('/' )
def index():
    # Serve the index.html page
    return render_template('index.html')
@app.route('/generate-image', methods=['POST'])
def generate_image():
    text_prompt = request.json.get('prompt')
    logging.info(f"Received prompt: {text_prompt}")

    if not text_prompt:
        return jsonify({"status": "error", "message": "No prompt provided"}), 400

    try:
        response = client.images.generate(
            model="dall-e-2",
            prompt=text_prompt,
            n=1,
            size="1024x1024"
        )
        logging.info(f"API Response: {response}")

        image_url = response.data[0].url
        logging.info("Image generated successfully.")
        return jsonify({"status": "success", "image_url": image_url})

    except Exception as e:
        logging.error(f"Error generating image: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

