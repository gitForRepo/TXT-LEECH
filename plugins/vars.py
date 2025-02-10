import os

API_ID    = os.environ.get("API_ID", 12283173515)
API_HASH  = os.environ.get("API_HASH", "be786a8240abf6e12283173515e2f833")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8113578720:AAGuDsG3Gqa6XkwurIFbQRX5y3LwrtbTeU8") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
