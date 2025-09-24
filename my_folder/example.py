
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler

# توكن البوت من BotFather
TOKEN = "8156729300:AAEn59qQjjGzdLL8uBRxaDEW0dAO7czYISI"


# دالة الرد على الرسائل
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    print("وصلت رسالة:", update.message.text)
    await update.message.reply_text(update.message.text)
    await update.message.reply_text(update.message.text)

# دالة التشغيل الرئيسية
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.add_handler(CommandHandler("start", echo))
    print ("الحمد لله البوت اشتغل...")
    app.run_polling()

if __name__ == "__main__":
    main()