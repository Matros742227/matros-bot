import json
import telebot

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

BOT_TOKEN = config.get("7740358299:AAER7Z0Wjh7NdZbcL7C11VNBQ_GAE9KJjgA")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Бот запущен. Я на связи!")

@bot.message_handler(func=lambda msg: True)
def echo(message):
    bot.reply_to(message, f"Ты написал: {message.text}")

if __name__ == "__main__":
    print("Bot is running…")
    bot.polling(none_stop=True)
