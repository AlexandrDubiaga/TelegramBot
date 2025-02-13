import telebot
from telebot import types
import webbrowser


bot = telebot.TeleBot('7563020591:AAF2dRoBBgGtzOHLKvOYRbQd0bn5AcCkqU0')

buttonForProfessional = types.InlineKeyboardMarkup()  # создаём кнопку
button1 = types.InlineKeyboardButton("Фахівець", url='http://t.me/Forlemm/')  # добавляем текст кнопки и ссылку
buttonForProfessional.add(button1)  # добавляем кнопку

buttonForPrice = types.InlineKeyboardMarkup()  # создаём кнопку
button2 = types.InlineKeyboardButton("Переглянути ціни тут!", url='http://expert.mmbti.com.ua/price/')  # добавляем текст кнопки и ссылку
buttonForPrice.add(button2)  # добавляем кнопку


markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
service = types.KeyboardButton("Послуги")
price = types.KeyboardButton("Ціни")
site = types.KeyboardButton("Чат з фахівцем")
markup.row(service, price, site)
adress = types.KeyboardButton('Адреси')
contact = types.KeyboardButton('Контакти')
sign = types.KeyboardButton('Залишити заявку')
markup.row(sign, adress,contact)

callProf = types.KeyboardButton('Дзвінок фахівцю')
markup.row(callProf)





@bot.message_handler(regexp='start')
def start(message):
    bot.send_message(message.chat.id,f'Вас вітає, КП "ММБТІ". {message.from_user.first_name}, оберіть, що вас цікавить:',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text == 'Контакти':bot.send_message(message.chat.id,f'Тисніть на номер телефону для дзвінка або на email, щоб надіслати повідомлення:\n\n'
                                                                   f'Моб: +380981871050\n'
                                                                   f'Приймальня: +380512470781\n'
                                                                   f'Email: office@mmbti.com.ua\n'
                                                                   f'Головний інженер: +380512470781\n'
                                                                   f'Головний бухгалтер: +380512471506\n'
                                                                   f'Відділ прийому громадян:+380512470967\n'
                                                                   f'Стіл замовлень: +380512722132\n'
                                                                   f'Сайт: http://expert.mmbti.com.ua/contact/\n\n ',reply_markup=markup)

    elif message.text == 'Послуги':bot.send_message(message.chat.id,f'- ТЕХНІЧНА ІНВЕНТАРИЗАЦІЯ НЕРУХОМОГО МАЙНА\n\n'
                                                                   f'- ОЦІНКА РУХОМОГО ТА НЕРУХОМОГО МАЙНА\n\n'
                                                                   f'- ТЕХНІЧНЕ ОБСТЕЖЕННЯ БУДІВЕЛЬ ТА СПОРУД\n\n'
                                                                    f'Детальніше переходь на наш Сайт, за посиланням:\n\n http://expert.mmbti.com.ua/\n\n',reply_markup=markup)


    elif message.text == 'Ціни': bot.send_message(message.chat.id, "Ціни на послуги", reply_markup=buttonForPrice)


    elif message.text == 'Чат з фахівцем':bot.send_message(message.chat.id, "Розпочати діалог?", reply_markup=buttonForProfessional)

    elif message.text == 'Дзвінок фахівцю':bot.send_message(message.chat.id, 'Тисніть на номер: +380981871050', parse_mode='Markdown', reply_markup=markup)



    elif message.text == 'Адреси':bot.send_message(message.chat.id,

            f"Адреса КП \"ММБТІ\":\n\n" 
                f"Місто Миколаїв, вулиця Шевченка, 40, 54000\n\n"
            f"Адреса підрозділу, що обслуговує об’єкти у Корабельному районі:\n\n"
            f"м. Миколаїв, проспект Богоявленський, 314\n\n"
            f'Детальніше переходь на наш Сайт, за посиланням:\n\n http://expert.mmbti.com.ua/adress/\n\n', reply_markup=markup)

    elif (message.text == 'Привіт' or message.text == 'Добрий день' or message.text == 'Здравствуйте' or message.text == 'Добрый день' or message.text == 'Вітаю')  :bot.send_message(message.chat.id,

        f"Вітаємо вас!\n"
            f"Оберіть будь ласка, що вас цікавить\n", reply_markup=markup)

    elif message.text == 'Залишити заявку':
        bot.send_message(message.chat.id, 'Введіть будь-ласка ваше: Ім\'я, телефон і послугу, яка вас цікавить. Наш фахівець з вами зв\'яжеться', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, forward)
    else: bot.send_message(message.chat.id,f'{message.from_user.first_name} ,я вас не розумію!Оберіть, будь-ласка послугу:',reply_markup=markup)


def forward(message):
    bot.forward_message(chat_id='@mmbti_work', from_chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(message.chat.id, "Дякую, ми з вами зв\'яжемося якомога скоріше", reply_markup=markup)




bot.polling(none_stop=True)




