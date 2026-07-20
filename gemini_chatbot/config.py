import os
import sys
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")
SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT")
DB_NAME = os.getenv("DB_NAME")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL")  # Default to a smaller model if not specified

if not DB_NAME:
    print("Security Error: DB_NAME is missing from your .env file!")
    print("Please add a database name to your .env file.")
    sys.exit(1)

if not GEMINI_API_KEY:
    print("Security Error: GEMINI_API_KEY is missing from your .env file!")
    print("Please generate a key at https://aistudio.google.com/ and add it to .env")
    sys.exit(1)