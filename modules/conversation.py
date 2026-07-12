from config.session import user_states
from modules.states import ASK_LOCATION


def start_conversation(user_id):
    user_states[user_id] = ASK_LOCATION

    return "📍 Welcome to Smart Travel Engine!\n\nWhere are you starting your journey?"
