import telebot
import config
from telebot import types
bot=telebot.TeleBot(config.TOKEN)
pizza = open('C:/Users/gusev/telbot/pizza.jpg','rb')
yupi = open('C:/Users/gusev/telbot/yupi.jpg','rb')
yupi1 = open('C:/Users/gusev/telbot/yupi.jpg','rb')
years = types.ReplyKeyboardMarkup(True,True)
yes_no = types.ReplyKeyboardMarkup(True,True)
yes_no1 = types.ReplyKeyboardMarkup(True,True)
yes_no2 = types.ReplyKeyboardMarkup(True,True)
yes_no3 = types.ReplyKeyboardMarkup(True,True)
pizzaK = types.ReplyKeyboardMarkup(True,True)
y18 = types.KeyboardButton('18 и больше')
y17 = types.KeyboardButton('меньше 18')
y35 = types.KeyboardButton('больше 35')
yes = types.KeyboardButton('да')
no = types.KeyboardButton('нет')
no1 = types.KeyboardButton('неа')
no2 = types.KeyboardButton('не хочу')
no3 = types.KeyboardButton('не очень')
yes1 = types.KeyboardButton('ну да')
yes2 = types.KeyboardButton('ага')
yes3 = types.KeyboardButton('очень')
yes4 = types.KeyboardButton('хочу')
pizza1 = types.KeyboardButton('сырная')
pizza2 = types.KeyboardButton('мясная')
pizza3 = types.KeyboardButton('пепперони')
years.add(y18,y17,y35)
yes_no.add(yes,no)
yes_no1.add(yes3,no2)
yes_no2.add(yes2,no1)
yes_no3.add(yes4,no3)
pizzaK.add(pizza1,pizza2,pizza3)
@bot.message_handler(commands=['start'])
def welc(message):
    bot.send_message(message.chat.id, "начнем небольшой тест")
    bot.send_message(message.chat.id, "сколько тебе лет", reply_markup=years)
@bot.message_handler(content_types=['text'])
def quiz(message):
    if message.text == 'меньше 18':
        years=types.ReplyKeyboardRemove(True)
        bot.send_message(message.chat.id,'хочешь конфетку',reply_markup=yes_no1)
    elif message.text == 'очень':
        bot.send_message(message.chat.id, '🍭')
    elif message.text == 'не хочу':
        bot.send_message(message.chat.id,'жалко')
    elif message.text == 'больше 35':
        years=types.ReplyKeyboardRemove(True)
        bot.send_message(message.chat.id,'Знаешь что такое юпи',reply_markup=yes_no2)
    elif message.text == 'ага':
        bot.send_message(message.chat.id,'хочешь?',reply_markup=yes_no3)
    elif message.text == 'хочу':
        bot.send_photo(message.chat.id, yupi)
    elif message.text == 'не очень':
        bot.send_message(message.chat.id,'жалко')
    elif message.text == 'неа':
        bot.send_message(message.chat.id,'вот что это такое')
        bot.send_photo(message.chat.id, yupi1)
    elif message.text == '18 и больше':
        years=types.ReplyKeyboardRemove(True)
        bot.send_message(message.chat.id,'какая пицца самая популярная',reply_markup=pizzaK)
    elif message.text == 'пепперони':
        bot.send_message(message.chat.id,'хочешь ее?',reply_markup=yes_no)
    elif message.text == 'да':
        bot.send_photo(message.chat.id, pizza)
    elif message.text == 'нет':
        bot.send_message(message.chat.id,'жалко')
    elif message.text == 'мясная':
        bot.send_message(message.chat.id,'правильный ответ пепперони')
    elif message.text == 'сырная':
        bot.send_message(message.chat.id,'правильный ответ пепперони')
bot.polling(none_stop=True)
