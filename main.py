from dotenv import load_dotenv

from modules.notifications import send_message
from modules.conversation import start_conversation

load_dotenv()

USER_ID = 1017503483

message = start_conversation(USER_ID)

send_message(message)
