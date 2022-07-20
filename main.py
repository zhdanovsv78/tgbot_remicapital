import telebot
from telebot import types
import datetime
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    text1 = f"Финансовая компания <b>РЕМИ КАПИТАЛ</b> приветствует Вас, {message.from_user.first_name}!\n\n" \
            "Мы выдаем кредиты для ЮР и ФЛ\n" \
            "- По-настоящему быстрое кредитование\n" \
            "- Лучшая альтернатива банкам\n" \
            "- Без лишних документов и проверок\n" \
            "- Состоим в реестре ЦБ РФ\n" \
            "- Помогаем развивать бизнес"
    bot.send_message(message.from_user.id, text1, parse_mode='html')

@bot.message_handler(commands=['about'])
def about(message):
    text = "Финансовая компания <b>РЕМИ КАПИТАЛ</b>:\n\n" \
            "Мы выдаем кредиты для ЮР и ФЛ\n" \
            "- По-настоящему быстрое кредитование\n" \
            "- Лучшая альтернатива банкам\n" \
            "- Без лишних документов и проверок\n" \
            "- Состоим в реестре ЦБ РФ"
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('💸 Условия займа', callback_data='zaym')
    btn2 = types.InlineKeyboardButton('🌐 Наш сайт', url='https://remicapital.ru')
    markup.row(btn1, btn2)
    video = open('./video.mp4', 'rb')
    bot.send_video(message.from_user.id, video)
    bot.send_message(message.from_user.id, text, reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['zaym'])
def zaym(message):
    text = f"🚗 <u>ПОД ЗАЛОГ АВТОМОБИЛЯ:</u>\n" \
            "- до 2 млн за 1 час\n" \
            "- авто остается у вас\n\n" \
            "🏡 <u>ПОД ЗАЛОГ НЕДВИЖИМОСТИ:</u>\n" \
            "- до 5 млн\n" \
            "- сроком до 5 лет\n\n" \
            "🤷 <u>БЕЗ ЗАЛОГА</u>\n" \
            "- до 3 млн\n" \
            "- для ООО и ИП"
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('🌐 Залог авто', url='https://remicapital.ru/auto/')
    btn2 = types.InlineKeyboardButton('🌐 Залог недв.', url='https://remicapital.ru/realty/')
    btn3 = types.InlineKeyboardButton('🌐 Без залога', url='https://remicapital.ru/bez_zaloga/')
    markup.row(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode='html')
    markup = telebot.types.ReplyKeyboardMarkup(True, True)

@bot.message_handler(commands=['contacts'])
def contacts(message):
    text = f"Название компании: <b>ООО МКК \"РЕМИ КАПИТАЛ\"\n</b>" \
            "ИНН/КПП: <b>1841084459 / 184101001\n</b>" \
            "ОГРН: <b>1191832004616\n</b>" \
            "Адрес: <b>426011, г. Ижевск, ул. 10 лет Октября, д. 23\n</b>" \
            "Телефон: <b>8 (3412) 32-69-43\n</b>" \
            "Email: <b>info@remi.capital\n</b>" \
            "Сайт: <b>https://remicapital.ru\n</b>" \
            "Режим работы: <b>09:00-18:00 будни</b>"
    markup = telebot.types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, text, parse_mode='html')

@bot.message_handler(commands=['lead'])
def lead(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('🏠 Ижевск', callback_data='izhevsk')
    btn2 = types.InlineKeyboardButton('🏠 Пермь', callback_data='perm')
    btn3 = types.InlineKeyboardButton('🏠 Н.Новгород', callback_data='nnovgorod')
    btn4 = types.InlineKeyboardButton('Отмена', callback_data='cancel')
    markup.row(btn1, btn2, btn3)
    markup.row(btn4)
    bot.send_message(message.from_user.id, 'Выберите город с нашим офисом:', reply_markup=markup, parse_mode='html')

@bot.callback_query_handler(func=lambda call: call.data == 'cancel')
def cancel_callback(call):
    if call.message:
        if call.data == "cancel":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Отменено.')
            bot.clear_step_handler(call.message)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "zaym":
        text1 = f"🚗 <u>ПОД ЗАЛОГ АВТОМОБИЛЯ:</u>\n" \
                "- до 2 млн за 1 час\n" \
                "- авто остается у вас\n\n" \
                "🏡 <u>ПОД ЗАЛОГ НЕДВИЖИМОСТИ:</u>\n" \
                "- до 5 млн\n" \
                "- сроком до 5 лет\n\n" \
                "🤷 <u>БЕЗ ЗАЛОГА</u>\n" \
                "- до 3 млн\n" \
                "- для ООО и ИП"

        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('🌐 Залог авто', url='https://remicapital.ru/auto/')
        btn2 = types.InlineKeyboardButton('🌐 Залог недв.', url='https://remicapital.ru/realty/')
        btn3 = types.InlineKeyboardButton('🌐 Без залога', url='https://remicapital.ru/bez_zaloga/')
        markup.row(btn1, btn2, btn3)
        bot.send_message(call.message.chat.id, text1, reply_markup=markup, parse_mode='html')
        markup = telebot.types.ReplyKeyboardMarkup(True, True)

    if call.data.startswith('izhevsk') or call.data.startswith('perm') or call.data.startswith('nnovgorod'):
        global answers, city
        if call.data == 'izhevsk':
            city = 'Ижевск'
        elif call.data == 'perm':
            city = 'Пермь'
        else:
            city = 'Н.Новгород'

        answers = []
        first_answer = city
        answers.append(first_answer)
        bot.send_message(call.message.chat.id, city)
        markup = telebot.types.InlineKeyboardMarkup()
        btn_cancel = types.InlineKeyboardButton('Отмена', callback_data='cancel')
        markup.row(btn_cancel)
        send = bot.send_message(call.message.chat.id, 'Как вас зовут? (Фамилия, Имя):', reply_markup=markup)
        bot.register_next_step_handler(send, two_q)

def two_q(message):
    two_answer = message.text
    answers.append(two_answer)

    markup = telebot.types.InlineKeyboardMarkup()
    btn_cancel = types.InlineKeyboardButton('Отмена', callback_data='cancel')
    markup.row(btn_cancel)
    send = bot.send_message(message.chat.id, 'Какая сумма кредита интересует?', reply_markup=markup)
    bot.register_next_step_handler(send, three_q)

def three_q(message):
    three_answer = message.text
    answers.append(three_answer)
    markup = telebot.types.InlineKeyboardMarkup()
    btn_cancel = types.InlineKeyboardButton('Отмена', callback_data='cancel')
    markup.row(btn_cancel)
    send = bot.send_message(message.chat.id, 'На какой срок?', reply_markup=markup)
    bot.register_next_step_handler(send, four_q)

def four_q(message):
    four_answer = message.text
    answers.append(four_answer)
    markup = telebot.types.InlineKeyboardMarkup()
    btn_cancel = types.InlineKeyboardButton('Отмена', callback_data='cancel')
    markup.row(btn_cancel)
    send = bot.send_message(message.chat.id, 'Ваш номер телефона?', reply_markup=markup)
    bot.register_next_step_handler(send, end)

def end(message):
    five_answer = message.text
    answers.append(five_answer)
    lid = '{}'.format('\n'.join(answers))
    now = datetime.datetime.now()
    lid = "<b>Заявка " + now.strftime("%d-%m-%Y %H:%M") + "</b>\n" + lid
    contact = f'<b>TG-данные</b>: ' + message.from_user.full_name + '\n' + '@' + message.from_user.username
    lid = lid + '\n' + contact
    bot.send_message("@remicapitalgrp", lid, parse_mode='html')

    msg = f'<b>Спасибо, ваша заявка успешно отправлена!</b>\n'\
    'Наши менеджеры скоро свяжутся с Вами.'

    keyboard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, msg, reply_markup=keyboard, parse_mode='html')
    markup = telebot.types.InlineKeyboardMarkup()

print('Runing')
bot.polling()

