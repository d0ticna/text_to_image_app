
from flask import Flask, Blueprint

import openai
from dotenv import load_dotenv
load_dotenv()
import os
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
  
    # Set the OpenAI API key
    openai.api_key = app.config['OPENAI_API_KEY']
    print("OpenAI API Key:", os.getenv('OPENAI_API_KEY'))
    

    from .routes import bp
    app.register_blueprint(bp)

    return app

    

  
