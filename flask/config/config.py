ENVIRONMENT = os.getenv('ENVIRONMENT', 'PRODUCTION').upper()

# Load configuration from .env file if in DEVELOPMENT environment
if ENVIRONMENT == 'DEVELOPMENT':
    # Assuming your .env file is two levels up from this script
    dotenv_path = os.path.join(os.path.dirname(__file__), '../../.env')
    load_dotenv(dotenv_path=dotenv_path)
