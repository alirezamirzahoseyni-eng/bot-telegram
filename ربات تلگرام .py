from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import telebot
import requests

TOKEN = "7967635730:AAFADY7dFEQk5JewBgo8cSVm3Ip9jE8phjw"
bot = telebot.TeleBot(TOKEN)

currency_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
currency_keyboard.add(KeyboardButton('BTCUSDT'), KeyboardButton('ETHUSDT'))
currency_keyboard.add(KeyboardButton('DOGEUSDT'), KeyboardButton('LTCUSDT'))
currency_keyboard.add(KeyboardButton('XRPUSDT'), KeyboardButton('BCHUSDT'))
currency_keyboard.add(KeyboardButton('LINKUSDT'), KeyboardButton('BNBUSDT'))
currency_keyboard.add(KeyboardButton('SOLUSDT'), KeyboardButton('TRXUSDT'))
currency_keyboard.add(KeyboardButton('MATICUSDT'), KeyboardButton('AVAXUSDT'))
currency_keyboard.add(KeyboardButton('DOTUSDT'))


def log_user_activity(user_id, username, action):
    with open("users.txt", "a", encoding="utf-8") as f:
        f.write(f"{user_id} | {username} | {action}\n")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    log_user_activity(message.from_user.id,
                      message.from_user.username, "start")
    bot.reply_to(
        message,
        'Hello dear, what currency do you want the price?(کس عمه زهرا)',
        reply_markup=currency_keyboard
    )


@bot.message_handler(func=lambda m: True)
def price(message):
    symbol = message.text.upper()
    log_user_activity(message.from_user.id,
                      message.from_user.username, f"asked {symbol}")
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
    respons = requests.get(url)
    if respons.status_code == 200:
        data = respons.json()
        bot.reply_to(message, f"{data['symbol']} price is {data['price']}")
    else:
        bot.reply_to(message, 'ورودی اشتباه است')


bot.polling()
