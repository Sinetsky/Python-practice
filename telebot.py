import telebot
import random

TOKEN = ""
bot = telebot.TeleBot(token=TOKEN)


guess = ["По моему мнению это ", "Я склонен предполагать, что это ", "Мне кажется это ",
         "Это определенно ", "Без сомнений это ", "Это никто иной как ", "Есть догадка, что это "]

greet = ["Приветствую ", "Рад видеть ", "Здравствуй ", "Привет ", "Какая встреча ", "Какие люди ",
         "Добрый день ", "Рад встрече "]

answers = ["Интересно", "Замечательная история", "Вижу у вас очень насыщенная жизнь",
           "Невероятно", "С вами есть о чем поговорить", "Вы прекрасный собеседник",
           "Отличная тема для обсуждения", "Я весь внимание", "Чудный день, не правда ли"]
who = ["Мегатрон", "мистер Проппер", "пингвин - снайпер", "конь с тремя руками", "подозрительный гном",
       "акула с крыльями", "танцор диско", "первый человек на марсе", "тушканчик - рестлер",
       "креветка - космонавт"]

@bot.message_handler(commands=['start'])
def starting(message):
    cid = message.chat.id
    bot.send_message(cid, 'Привет, я бот Лакей, версия 2.0 \nНа данный момент я нахожусь в разработке, '
                          'но мои возможности с каждым днем улучшаются.\nКак со мной общаться:\n1. Добавь'
                          ' меня в группу\n2. Начните переписываться\n3. Спроси меня "Лакей, кто...", '
                          'и я дам тебе ответ.')

@bot.message_handler(content_types=['text'])
def answer(message):
    cid = message.chat.id
    text = message.text.lower()
    name = message.from_user.first_name
    if "лакей" in text:
        if "кто" in text:
            bot.send_message(cid, random.choice(guess) + random.choice(who))
        elif "привет" in text:
            bot.send_message(cid, greet[random.randint(0, 7)] + name)
    if "я " in text:
            bot.send_message(cid, answers[random.randint(0, 8)])

bot.polling(none_stop=True, interval=0)