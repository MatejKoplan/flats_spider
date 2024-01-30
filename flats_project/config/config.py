import os
from dotenv import load_dotenv

DEVELOPMENT_ENV = 'DEVELOPMENT'
PRODUCTION_ENV = 'PRODUCTION'

# Determine the environment
ENVIRONMENT = os.getenv('ENVIRONMENT', PRODUCTION_ENV).upper()


# Load configuration from .env file if in DEVELOPMENT environment
if ENVIRONMENT == DEVELOPMENT_ENV:
    # Assuming your .env file is two levels up from this script
    dotenv_path = os.path.join(os.path.dirname(__file__), '../../.env')
    load_dotenv(dotenv_path=dotenv_path)

# Configuration variables
POSTGRES_DB = os.getenv('POSTGRES_DB', 'sreality')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'myuser')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
