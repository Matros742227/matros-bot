import os
import telebot

# Читаем токен из переменной среды, установленной в Render
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")

if not BOT_TOKEN:
    raise ValueError("TELEGRAM_TOKEN отсутствует в переменных среды!")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Бот запущен. Я на связи!")

@bot.message_handler(func=lambda msg: True)
def echo(message):
    bot.reply_to(message, f"Ты написал: {message.text}")

if __name__ == "__main__":
    print("Bot is running...")
    bot.polling(non_stop=True)

