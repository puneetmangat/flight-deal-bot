from dotenv import load_dotenv

from modules.receiver import get_updates

load_dotenv()

updates = get_updates()

print(updates)
