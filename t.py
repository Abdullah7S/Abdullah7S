from telegram import Update
     from telegram.ext import Updater, CommandHandler, CallbackContext

     TOKEN = '7779401366:AAFXy0YWgUzXnABHrkpE23qaEmBOn21dq5c'  # استبدل YOUR_TOKEN_HERE بالتوكن الخاص بك

     def start(update: Update, context: CallbackContext) -> None:
         update.message.reply_text('Hello! I am your bot.')

     def main():
         updater = Updater(TOKEN)

         dispatcher = updater.dispatcher
         dispatcher.add_handler(CommandHandler("start", start))

         updater.start_polling()
         updater.idle()

     if __name__ == '__main__':
         main()
