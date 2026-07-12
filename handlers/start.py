from telegram import Update
from telegram.ext import ContextTypes

from config.session import user_states
from modules.states import ASK_LOCATION


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    user_states[user_id] = ASK_LOCATION

    await update.message.reply_text(
        "📍 Welcome to Smart Travel Engine!\n\nWhere are you starting your journey?"
    )
