import telebot 
from dotenv import load_dotenv
from model.main import spellchecker

load_dotenv()
token="5659615815:AAF8UzRc-XW6Ds2yk24TU7cbmeVDJN-FkHM"
bot=telebot.TeleBot(token=token)

@bot.message_handler(content_types=['text'])

def message_recieved(message):
    
    if message.text=="exit":
        exit(0)
    elif message.text=="hello":
        bot.send_message(chat_id=message.from_user.id,text=" Hello "+message.from_user.username)
    else:
          
         bot.send_message(chat_id=message.from_user.id,text=spellchecker(message.text) )
    
bot.polling(True)
