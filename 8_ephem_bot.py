"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import settings
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def planets(update, context):
    planet_name = update.message.text.split(" ")
    planet_name = planet_name[-1]
    current_datetime = datetime.now()
    if planet_name == "Mercury":
        planet = ephem.Mercury(current_datetime)
    if planet_name == "Venus":
        planet = ephem.Venus(current_datetime)
    if planet_name == "Earth":
        planet = ephem.Earth(current_datetime)
    if planet_name == "Mars":
        planet = ephem.Mars(current_datetime)
    if planet_name == "Jupiter":
        planet = ephem.Jupiter(current_datetime)
    if planet_name == "Saturn":
        planet = ephem.Saturn(current_datetime)
    if planet_name == "Uranus":
        planet = ephem.Uranus(current_datetime)
    if planet_name == "Neptune":
        planet = ephem.Neptune(current_datetime)
    constellation = ephem.constellation(planet)
    print(constellation)
    update.message.reply_text(constellation)

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)
 

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planets))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
