# server/utils/envars.py

import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent.parent / ".env")

ENV_MODE = os.getenv("ENV_MODE", "production")
OMDB_API_KEY = os.getenv("OMDB_API_KEY", "")
