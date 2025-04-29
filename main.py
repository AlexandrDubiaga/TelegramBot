import telebot
from telebot import types


bot = telebot.TeleBot('7563020591:AAF2dRoBBgGtzOHLKvOYRbQd0bn5AcCkqU0')


#Чат з  фахівцем
buttonForProfessional = types.InlineKeyboardMarkup()  # создаём кнопку
button1 = types.InlineKeyboardButton("(Натисни тут) ← Фахівець", url='http://t.me/OFFICE_MMBTI/')  # добавляем текст кнопки и ссылку
buttonForProfessional.add(button1)  # добавляем кнопку

#Ціни
buttonForPrice = types.InlineKeyboardMarkup()  # создаём кнопку
button2 = types.InlineKeyboardButton("(Натисни тут) ← Ціни", url='http://mmbti.com.ua/price/#prices')  # добавляем текст кнопки и ссылку
buttonForPrice.add(button2)  # добавляем кнопку

#Наш сайт
buttonForSite = types.InlineKeyboardMarkup()  # создаём кнопку
button3 = types.InlineKeyboardButton("(Натисни тут) ← Сайт", url='http://mmbti.com.ua/')  # добавляем текст кнопки и ссылку
buttonForSite.add(button3)  # добавляем кнопку

#Послуги
buttonForPosluga = types.InlineKeyboardMarkup()  # создаём кнопку
button4 = types.InlineKeyboardButton("(Натисни тут) ← Послуги", url='http://mmbti.com.ua/works/#works')  # добавляем текст кнопки и ссылку
buttonForPosluga.add(button4)  # добавляем кнопку

#Карта громад
buttonForMaps = types.InlineKeyboardMarkup()  # создаём кнопку
button5 = types.InlineKeyboardButton("(Натисни тут) ← Карта", url='http://mmbti.com.ua/#main-map')  # добавляем текст кнопки и ссылку
buttonForMaps.add(button5)  # добавляем кнопку

#Адреси
buttonForAddress = types.InlineKeyboardMarkup()  # создаём кнопку
button6 = types.InlineKeyboardButton("(Натисни тут) ← Адреси", url='http://mmbti.com.ua/adress/#adress')  # добавляем текст кнопки и ссылку
buttonForAddress.add(button6)  # добавляем кнопку






markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

chatWithProff = types.KeyboardButton("Чат з фахівцем")
callProf = types.KeyboardButton('Дзвінок фахівцю')
markup.row( chatWithProff,callProf)


service = types.KeyboardButton("Послуги")
ourSite = types.KeyboardButton('Наш сайт')
ourMapGromad = types.KeyboardButton('Карта громад')
markup.row(service, ourSite, ourMapGromad)


price = types.KeyboardButton("Ціни")
adress = types.KeyboardButton('Адреси')
contact = types.KeyboardButton('Контакти')
#sign = types.KeyboardButton('Залишити заявку')
markup.row(price, adress,contact)





@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Вас вітає, КП "ММБТІ". {message.from_user.first_name}, оберіть, що вас цікавить:', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text_message(message):


    if message.text == 'Чат з фахівцем': bot.send_message(message.chat.id, "Розпочати діалог? ↓↓↓↓", reply_markup=buttonForProfessional)
    elif message.text == 'Дзвінок фахівцю': bot.send_message(message.chat.id, 'Тисніть на номер:→→→ +380981871050', parse_mode='Markdown',reply_markup=markup)



    elif message.text == 'Послуги': bot.send_message(message.chat.id,"Наші послуги ↓↓↓↓",reply_markup=buttonForPosluga)
    elif message.text == 'Наш сайт': bot.send_message(message.chat.id, 'Переходь на сайт ↓↓↓↓', parse_mode='Markdown', reply_markup=buttonForSite)
    elif message.text == 'Карта громад': bot.send_message(message.chat.id, "Карта громад ↓↓↓↓", reply_markup=buttonForMaps)


    elif message.text == 'Ціни': bot.send_message(message.chat.id, "Ціни на послуги ↓↓↓↓", reply_markup=buttonForPrice)
    elif message.text == 'Адреси': bot.send_message(message.chat.id,'Наші адреси ↓↓↓↓', reply_markup=buttonForAddress)
    elif message.text == 'Контакти':bot.send_message(message.chat.id,f'Тисніть на номер телефону для дзвінка або на email, щоб надіслати повідомлення:\n\n'
                                                                   f'Моб: +380981871050\n'
                                                                   f'Приймальня: +380512470781\n'
                                                                   f'Email: office@mmbti.com.ua\n'
                                                                   f'Головний інженер: +380512470781\n'
                                                                   f'Головний бухгалтер: +380512471506\n'
                                                                   f'Відділ прийому гром.:+380512470967\n'
                                                                   f'Стіл замовлень: +380512722132\n\n',reply_markup=markup)








    elif (message.text == 'Привіт' or message.text == 'Добрий день' or message.text == 'Здравствуйте' or message.text == 'Добрый день' or message.text == 'Вітаю')  :bot.send_message(message.chat.id,

        f"Вітаємо вас!\n"
            f"Оберіть будь ласка, що вас цікавить\n", reply_markup=markup)

    #elif message.text == 'Залишити заявку':
     #   bot.send_message(message.chat.id, 'Введіть будь-ласка ваше: Ім\'я, телефон і послугу, яка вас цікавить. Наш фахівець з вами зв\'яжеться', reply_markup=types.ReplyKeyboardRemove())
     #   bot.register_next_step_handler(message, forward)


    else: bot.send_message(message.chat.id,f'{message.from_user.first_name} ,я вас не розумію!Оберіть, будь-ласка послугу:',reply_markup=markup)


def forward(message):
    bot.forward_message(chat_id='@mmbti_work', from_chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(message.chat.id, "Дякую, ми з вами зв\'яжемося якомога скоріше", reply_markup=markup)



bot.remove_webhook()
bot.polling(none_stop=True)




