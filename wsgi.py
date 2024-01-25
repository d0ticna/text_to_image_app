from app import create_app  # Import your Flask app creation function
from dotenv import load_dotenv
load_dotenv()
app = create_app()
# Load environment variables from .env file

# Ensure this is the entry point for the WSGI server
if __name__ == "__main__":
    app.run()
