# routes.py

from flask import Blueprint, jsonify,request
import logging
import openai

bp = Blueprint('bp', __name__, url_prefix='/')

@bp.route('/generate-image', methods=['POST'])
def generate_image():
    text_prompt = request.json.get('prompt')

    if not text_prompt:
        return jsonify({"status": "error", "message": "No prompt provided"}), 400

    try:
        
        response = openai.Image.create(
            model="dall-e-2",  
            prompt=text_prompt,
            n=1,
            size="1024x1024"
        )

        image_url = response['data'][0]['url']
        logging.info("Image generated successfully.")
        return jsonify({"status": "success", "image_url": image_url})
    except Exception as e:
        logging.error(f"Error generating image: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500
