import telebot
from telebot import types
import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # завантаження .env файлу

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = telebot.TeleBot(BOT_TOKEN)

# Главное меню (ReplyKeyboard)
main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.row(
    types.KeyboardButton("Чат з фахівцем"),
    types.KeyboardButton("Дзвінок фахівцю"),
    types.KeyboardButton("Написати листа")
)
main_menu.row(
    types.KeyboardButton("Послуги"),
    types.KeyboardButton("Наш сайт"),
    types.KeyboardButton("Карта громад")
)
main_menu.row(
    types.KeyboardButton("Ціни"),
    types.KeyboardButton("Адреси"),
    types.KeyboardButton("Контакти")
)



@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("start_log.txt", "a", encoding="utf-8") as file:
        file.write(f"{time_now} - {user_name} (ID: {user_id}) натиснув /start\n")

        # Повідомлення ТІЛЬКИ адміну
        if user_id != ADMIN_ID:
            try:
                bot.send_message(
                    ADMIN_ID,
                    f"🔔 Бот запустив:\n👤 {user_name} (ID: {user_id})\n🕒 {time_now}"
                )
            except Exception as e:
                print(f"⚠️ Помилка надсилання адміну: {e}")


    bot.send_message(
        message.chat.id,
        f'Вас вітає, КП "ММБТІ". {user_name}, оберіть, що вас цікавить:',
        reply_markup=main_menu
    )

@bot.message_handler(commands=['chat'])
def handle_chat(message):
    send_chat_link(message)

@bot.message_handler(commands=['call'])
def handle_call(message):
    send_call_info(message)

@bot.message_handler(commands=['email'])
def handle_email(message):
    send_email_link(message)

@bot.message_handler(commands=['services'])
def handle_services(message):
    send_services_link(message)

@bot.message_handler(commands=['website'])
def handle_website(message):
    send_website_link(message)

@bot.message_handler(commands=['map'])
def handle_map(message):
    send_map_link(message)

@bot.message_handler(commands=['prices'])
def handle_prices(message):
    send_price_link(message)

@bot.message_handler(commands=['addresses'])
def handle_addresses(message):
    send_address_link(message)

@bot.message_handler(commands=['contacts'])
def handle_contacts(message):
    send_contact_info(message)


@bot.message_handler(func=lambda message: message.text == 'Чат з фахівцем')
def send_chat_link(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Зв'язатись з фахівцем", url='http://t.me/OFFICE_MMBTI/')
    markup.add(button)
    bot.send_message(message.chat.id, "Розпочати діалог:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Дзвінок фахівцю')
def send_call_info(message):
    bot.send_message(
        message.chat.id,
        'Номер телефону фахівця:\n📞 +380981871050\n\nНатисніть на номер для дзвінка (з мобільного пристрою).'
    )


@bot.message_handler(func=lambda message: message.text == 'Написати листа')
def send_email_link(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Написати листа", url='http://mmbti.com.ua/contact/#contact-id')
    markup.add(button)
    bot.send_message(message.chat.id, "Залишити звернення:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Послуги')
def send_services_link(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Переглянути послуги", url='http://mmbti.com.ua/works/#works')
    markup.add(button)
    bot.send_message(message.chat.id, "Наші послуги:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Наш сайт')
def send_website_link(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Перейти на сайт", url='http://mmbti.com.ua/')
    markup.add(button)
    bot.send_message(message.chat.id, "Офіційний сайт:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Карта громад')
def send_map_link(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Відкрити карту", url='http://mmbti.com.ua/#main-map')
    markup.add(button)
    bot.send_message(message.chat.id, "Карта громад:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Ціни')
def send_price_link(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Перейти до цін", url='http://mmbti.com.ua/price/#prices')
    markup.add(button)
    bot.send_message(message.chat.id, "Ціни на послуги:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Адреси')
def send_address_link(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Дивитись адреси", url='http://mmbti.com.ua/adress/#adress')
    markup.add(button)
    bot.send_message(message.chat.id, "Наші адреси:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Контакти')
def send_contact_info(message):
    contact_text = (
        "<b>📞 Телефони для зв'язку:</b>\n\n"
        "📱 <b>Мобільний:</b> +380981871050\n"
        "📍 <b>Приймальня:</b> +380512470781\n"
        "🛠 <b>Голов. інженер:</b> +380512470781\n"
        "💼 <b>Голов. бухгалтер:</b> +380512471506\n"
        "🧾 <b>Стіл замовлень:</b> +380512722132\n"
        "👥 <b>Прийом громадян:</b> +380512470967\n\n"
        "✉️ <b>Email:</b> office@mmbti.com.ua"
    )
    bot.send_message(message.chat.id, contact_text, parse_mode="HTML")


@bot.message_handler(func=lambda message: message.text in ['Привіт', 'Добрий день', 'Здравствуйте', 'Добрый день', 'Вітаю'])
def greet_user(message):
    bot.send_message(
        message.chat.id,
        "Вітаємо вас!\nОберіть будь ласка, що вас цікавить",
        reply_markup=main_menu
    )


@bot.message_handler(func=lambda message: True)
def unknown_message(message):
    bot.send_message(
        message.chat.id,
        f"{message.from_user.first_name}, я вас не розумію! Оберіть, будь ласка, послугу:",
        reply_markup=main_menu
    )





# Запуск бота
bot.remove_webhook()
bot.polling(none_stop=True)

