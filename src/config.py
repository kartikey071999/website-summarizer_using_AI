import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define constants
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "default_key_if_missing")
DATABASE_URL = os.getenv("DATABASE_URL")
DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() in ("true", "1")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
