from dotenv import load_dotenv
from modules.notifications import send_message
from modules.planner import create_trip

load_dotenv()

trip = create_trip()

send_message(trip)
