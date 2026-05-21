import telebot
from dotenv import load_dotenv
import os
from random import choice


load_dotenv()
bot = telebot.TeleBot(os.getenv('TG_API_TOKEN'))


@bot.message_handler(commands=['start'])
def send_welcome(message):
#    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь! Команды : /bye ends the bot, /tips")
    bot.reply_to(message, f'Привет! Я бот который хочет предупредить что глобальное потепление это важная проблемаю Команды : /start starts the bot, /image sends an image')

@bot.message_handler(commands=['explain'])
def send_explain(message):
#    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь! Команды : /bye ends the bot, /tips")
    bot.reply_to(message, """Глобальное потепление - это процесс повышения средней температуры атмосферы и океанов Земли, вызванный увеличением концентрации парниковых газов, таких как углекислый газ, метан и другие.
Это приводит к изменению климата, таянию ледников, повышению уровня моря и другим экологическим проблемам.
Важно принимать меры для снижения выбросов парниковых газов и адаптации к изменениям климата, чтобы сохранить нашу планету для будущих поколений.""")


@bot.message_handler(commands=['image'])
def send_image(message):
    random_image = choice(os.listdir('images'))
    with open(f'images/{random_image }', 'rb') as f:
        bot.send_photo(message.chat.id, f)

bot.polling()