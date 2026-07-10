from dotenv import load_dotenv
from modules.notifications import send_message

load_dotenv()

send_message("🎉 Flight Deal Bot is working securely!")
