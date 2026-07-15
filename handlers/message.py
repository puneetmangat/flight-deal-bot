from telegram import Update
from telegram.ext import ContextTypes

from modules.conversation_engine import (
    save_answer,
    next_question,
    get_current_question,
    is_complete,
    get_answers,
)
from modules.profile import build_profile


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    save_answer(user_id, text)

    next_question(user_id)

    if is_complete(user_id):
        answers = get_answers(user_id)
        profile = build_profile(answers)
        trip = profile["trip"]

        summary = (
            "✅ Smart Travel Engine\n\n"
            f"📍 Departure: {trip['departure']}\n"
            f"🌍 Destination: {trip['destination']}\n"
            f"🎯 Goal: {trip['goal']}\n"
            f"📅 Dates: {trip['dates']}\n"
            f"💰 Budget: {trip['budget']}"
        )

        await update.message.reply_text(summary)
        return

    question = get_current_question(user_id)

    await update.message.reply_text(question["text"])
