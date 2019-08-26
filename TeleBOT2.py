import pyowm
import telebot

owm = pyowm.OWM('0f1d3a200ded5a670c2754d000090022', language = "ru")
bot = telebot.TeleBot("960561528:AAF6XUqrzn5PZ-Ql8gL123gFTdjl3-GFvV0")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation =  owm.weather_at_place( message.text )
    w =  observation.get_weather()
    temp = w.get_temperature('celsius')["temp"] 

    answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
    answer += "Температура сейчас в районе " + str(temp) + "\n\n"

    if temp < 10:
        answer += "Сечас довольно холодно, одевайся теплее. "
    elif temp < 20:
        answer += "Сейчас вполне норм, но не для шорт. "
    else:
        answer += "Жарко, расплавишься. "

    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )    