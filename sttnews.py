import telebot
from telebot import types

#1765191368:AAGzh1_qZxz9ALViIbF2v3_NNQVOtZmSjPM



bot = telebot.TeleBot('1765191368:AAGzh1_qZxz9ALViIbF2v3_NNQVOtZmSjPM')

result = []


@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.from_user.id, 'Напишите "Старт" для начала расчета')
    bot.register_next_step_handler(message, get_auto)


def get_auto(message):
    if message.text == 'Старт':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        auto1 = types.KeyboardButton('Газель Некст')
        auto2 = types.KeyboardButton('Газон Некст')
        auto3 = types.KeyboardButton('Садко')
        auto4 = types.KeyboardButton('Газель Бизнес')
        auto5 = types.KeyboardButton('ГАЗ 4х4')
        keyboard.add(auto1, auto2, auto3, auto4, auto5,)
        bot.send_message(message.chat.id, 'Какой автомобиль вы хотели бы приобрести?', reply_markup=keyboard)
        bot.register_next_step_handler(message, )
    else:
        bot.send_message(message.from_user.id, 'Вернитесь в начало')



bot.polling()