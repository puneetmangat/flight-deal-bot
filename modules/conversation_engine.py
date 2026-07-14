from config.session import user_sessions
from modules.questions import QUESTIONS


def start_session(user_id):
    user_sessions[user_id] = {
        "current_question": QUESTIONS[0]["id"],
        "answers": {}
    }


def get_current_question(user_id):
    session = user_sessions[user_id]
    current_id = session["current_question"]

    for question in QUESTIONS:
        if question["id"] == current_id:
            return question

    return None


def save_answer(user_id, answer):
    session = user_sessions[user_id]

    question = get_current_question(user_id)

    session["answers"][question["id"]] = answer


def next_question(user_id):
    session = user_sessions[user_id]

    current_id = session["current_question"]

    for index, question in enumerate(QUESTIONS):
        if question["id"] == current_id:

            if index + 1 < len(QUESTIONS):
                session["current_question"] = QUESTIONS[index + 1]["id"]
                return

            session["current_question"] = None
            return

def is_complete(user_id):
    session = user_sessions[user_id]
    return session["current_question"] is None


def get_answers(user_id):
    return user_sessions[user_id]["answers"]

