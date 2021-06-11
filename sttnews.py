import telebot
from telebot import types

#1765191368:AAGzh1_qZxz9ALViIbF2v3_NNQVOtZmSjPM

bot = telebot.TeleBot('1765191368:AAGzh1_qZxz9ALViIbF2v3_NNQVOtZmSjPM')

res = []


@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.from_user.id, 'Напишите "Старт" для начала расчета')
    bot.register_next_step_handler(message, get_auto)


def get_auto(message):
    if message.text == 'Старт':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        costauto1 = types.KeyboardButton('Газель Некст')
        costauto2 = types.KeyboardButton('Газон Некст')
        costauto3 = types.KeyboardButton('Садко')
        costauto4 = types.KeyboardButton('Газель Бизнес')
        costauto5 = types.KeyboardButton('ГАЗ 4х4')
        keyboard.add(costauto1, costauto2, costauto3, costauto4, costauto5,)
        bot.send_message(message.chat.id, 'Какой автомобиль вы хотели бы приобрести?', reply_markup=keyboard)
        bot.register_next_step_handler(message, get_costauto)
    else:
        bot.send_message(message.from_user.id, 'Вернитесь в начало')

def get_costauto(message):
	if message.text == 'Газель Некст':
		sum = 1751000
		res.append(sum)
	elif message.text == 'Газон Некст':
		sum = 2244800
		res.append(sum)
	elif message.text == 'Садко':
		sum = 2356900
		res.append(sum)
	elif message.text == 'Газель Бизнес':
		sum = 1368300
		res.append(sum)
	else:
		sum = 2536600
		res.append(sum)
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	service_contract1 = types.KeyboardButton('Да')
	service_contract2 = types.KeyboardButton('Нет')
	keyboard.add(service_contract1, service_contract2)
	bot.send_message(message.chat.id, 'Хотите добавить сервисный контракт?', reply_markup = keyboard)
	bot.register_next_step_handler(message, get_finish)

def get_finish(message):
	if message.text == 'Да':
		contract1 = 252350
		res.append(contract1)
	else:
		contract2 = 0
		res.append(contract2)
	bot.send_message(message.from_user.id, 'Отлично!')
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	Itogo = types.KeyboardButton('Итоговая стоимость')
	keyboard.add(Itogo)
	bot.send_message(message.chat.id, 'Нажмите "Итоговая стоимость", чтобы получить стоимость автомобиля', reply_markup = keyboard)
	bot.register_next_step_handler(message, finish)
def finish(message):
	Summa = int(res[0]+res[1])
	bot.send_message(message.from_user.id, 'Сумма вашего платежа')
	bot.send_message(message.chat.id, Summa)

bot.polling()