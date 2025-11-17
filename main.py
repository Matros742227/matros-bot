import json
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from openai import OpenAI

# Загружаем токены из config.json
with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

TELEGRAM_TOKEN = config["TELEGRAM_TOKEN"]
OPENAI_API_KEY = config["OPENAI_API_KEY"]

# Настройка OpenAI клиента
client = OpenAI(api_key=OPENAI_API_KEY)

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот запущен! Пиши что-нибудь — отвечу через GPT 😊")

async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_text}]
    )

    bot_reply = response.choices[0].message.content
    await update.message.reply_text(bot_reply)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler(None, answer))

    app.run_polling()


