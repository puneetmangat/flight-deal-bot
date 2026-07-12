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
