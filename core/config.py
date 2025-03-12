"""
Configuration settings
"""

import os
from dotenv import load_dotenv
import pathlib

# Load environment variables
load_dotenv()


class Settings:
    # General
    BASE_DIR = str(pathlib.Path(__file__).parent.parent)
    MODELS_DIR = BASE_DIR + "/models"
    DEBUG = int(os.getenv("DEBUG", "0"))

    # API
    API_URL = os.getenv("API_URL")

    # Sentry
    SENTRY_DSN = os.getenv("SENTRY_DSN")

    # Logging
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "WARNING")


settings = Settings()
