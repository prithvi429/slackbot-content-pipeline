import os
from dotenv import load_dotenv

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN", "")
SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
FLASK_PORT = int(os.getenv("FLASK_PORT", "8080"))
REPORT_DIR = os.getenv("REPORT_DIR", ".")

