
import telegram.ext 

telegram_bot_token="5659615815:AAF8UzRc-XW6Ds2yk24TU7cbmeVDJN-FkHM"

updater = telegram.ext.Updater(token=telegram_bot_token, use_context=True)

dispatcher = updater.dispatcher

def start(update,context):
    
    update.message.reply_text("Hello Welcome to KatebSabaBot")
        
def help(update,context) :
    update.message.reply_text(
        
    """/start -> Welcome to the KatebSaba
       /help  -> This particular message 
       /content -> About my first chatbot with python 
       /EchoBot  -> EchoBot just responds by replying with the same message it receives
       /contact  -> contact info
    """
    ) 
      
     
def content(update,context):
    update.message.reply_text("my first chatbot in intrenship Cycle is available now!")      
    
def EchoBot(update,context):
    update.message.reply_text("you must have been done this task yesterday")    
    
    
def contact(update,context):
    update.message.reply_text("you can connect with me by this Email Address:sabapopolopolis@gmail.com")  
    
dispatcher.add_handler(telegram.ext.CommandHandler('start',start)) 
dispatcher.add_handler(telegram.ext.CommandHandler('help',help)) 
dispatcher.add_handler(telegram.ext.CommandHandler('content',content)) 
dispatcher.add_handler(telegram.ext.CommandHandler('EchoBot',EchoBot))    
dispatcher.add_handler(telegram.ext.CommandHandler('contact',contact))        

# start polling for updates from Telegram
updater.start_polling()
# block until a signal (like one sent by CTRL+C) is sent
updater.idle()