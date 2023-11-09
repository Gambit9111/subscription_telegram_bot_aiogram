import os
from dotenv import load_dotenv
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
WEB_SERVER_HOST= os.getenv("WEB_SERVER_HOST")
WEB_SERVER_PORT= os.getenv("WEB_SERVER_PORT")
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

if TELEGRAM_BOT_TOKEN is None:
    raise ValueError("Please set TELEGRAM_BOT_TOKEN environment variable")
elif WEBHOOK_URL is None:
    raise ValueError("Please set WEBHOOK_URL environment variable")
elif WEB_SERVER_PORT is None:
    raise ValueError("Please set WEB_SERVER_PORT environment variable")
elif WEB_SERVER_HOST is None:
    raise ValueError("Please set WEB_SERVER_HOST environment variable")
elif WEBHOOK_PATH is None:
    raise ValueError("Please set WEBHOOK_PATH environment variable")
elif WEBHOOK_SECRET is None:
    raise ValueError("Please set WEBHOOK_SECRET environment variable")
else:
    print("All environment variables are set \n")