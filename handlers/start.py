from telegram import Update
from telegram.ext import ContextTypes

from modules.conversation_engine import (
    start_session,
    get_current_question,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    start_session(user_id)

    question = get_current_question(user_id)

    await update.message.reply_text(question["text"])

