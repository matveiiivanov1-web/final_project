import telebot
from dotenv import load_dotenv
import os
from random import choice


load_dotenv()
bot = telebot.TeleBot(os.getenv('TG_API_TOKEN'))


@bot.message_handler(commands=['start'])
def send_welcome(message):
#    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь! Команды : /bye ends the bot, /tips")
    bot.reply_to(message, f'Привет! Я бот который хочет предупредить что глобальное потепление это важная проблема. Команды : /start starts the bot, /image sends an image related to global warming, /explain explains what global warming is, /tips gives tips on how to help, /facts shares interesting facts about global warming, /quiz starts a quiz about global warming, /bye ends the bot.')

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

@bot.message_handler(commands=['tips'])
def send_tips(message):
    bot.reply_to(message, "Вот несколько советов по борьбе с глобальным потеплением:\n-" \
    " Используйте общественный транспорт или велосипед.\n-" \
    " Сократите потребление энергии.\n- " \
    "Перерабатывайте отходы.\n-" \
    " Поддерживайте компании, которые занимаются экологией.")


facts = [
    "За последние 100 лет температура Земли выросла примерно на 1.1°C.",
    "Ледники тают быстрее из-за повышения температуры.",
    "Уровень мирового океана постепенно повышается.",
    "Лесные пожары становятся чаще из-за жары."
]
@bot.message_handler(commands=['facts'])
def send_facts(message):
    random_fact = choice(facts)
    bot.reply_to(message, random_fact)

quiz_questions = [
    {   "question": "Какой газ является основным парниковым газом?",
        "options": ["1. Углекислый газ", "2. Водород", "3. Азот"],
        "answer": "1. Углекислый газ"  
    },
    {   "question": "Какой сектор экономики является крупнейшим источником выбросов парниковых газов?",
        "options": ["1. Транспорт", "2. Сельское хозяйство", "3. Энергетика"],
        "answer": "3. Энергетика"
    },
    {   "question": "Какой из следующих процессов способствует глобальному потеплению?",
        "options": ["1. Вырубка лесов", "2. Сохранение энергии", "3. Переработка отходов"],
        "answer": "1. Вырубка лесов"
    }
]

@bot.message_handler(commands=['quiz'])
def quiz(message):
    question = choice(quiz_questions)
    options_text = "\n".join(question["options"])
    bot.reply_to(message, f"{question['question']}\n{options_text}")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Надеюсь, мы еще увидимся.")
    bot.stop_polling()

bot.polling()
