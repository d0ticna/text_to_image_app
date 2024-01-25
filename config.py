import os
class Config:
    # Fetch from environment variable
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

    """Base configuration."""

    
    # OpenAI configurations
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'dall-e-3')  # Default model for image generation
    IMAGE_GENERATION_ENDPOINT = os.getenv('IMAGE_GENERATION_ENDPOINT', 'http://localhost:5000/generate-image')

    # Image generation settings
    DEFAULT_IMAGE_SIZE = "800x800"  # Default image size
    MAX_GENERATED_IMAGES = int(os.getenv('MAX_GENERATED_IMAGES', 1))  # Max number of images to generate in one request

 
