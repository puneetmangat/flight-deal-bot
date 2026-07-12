from telegram import Update
from telegram.ext import ContextTypes

from config.session import user_states
from modules.states import ASK_LOCATION, ASK_GOAL, ASK_DESTINATION


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    state = user_states.get(user_id)

    if state == ASK_LOCATION:
        context.user_data["location"] = text
        user_states[user_id] = ASK_GOAL

        await update.message.reply_text(
            "🎯 What's your travel goal?"
        )

    elif state == ASK_GOAL:
        context.user_data["goal"] = text
        user_states[user_id] = ASK_DESTINATION

        await update.message.reply_text(
            "🌍 Where do you want to go?"
        )

    elif state == ASK_DESTINATION:
        context.user_data["destination"] = text

        await update.message.reply_text(
            f"✅ Trip Summary\n\n"
            f"📍 From: {context.user_data['location']}\n"
            f"🎯 Goal: {context.user_data['goal']}\n"
            f"🌍 Destination: {context.user_data['destination']}"
        )

    else:
        await update.message.reply_text(
            "Please type /start to begin."
        )
