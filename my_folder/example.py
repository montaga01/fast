
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# توكن البوت من BotFather
TOKEN = "8184537983:AAFmdN6BTH71K1jAqko46C7P5q9lFr3gldg"

# دالة الرد على الرسائل
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

# دالة التشغيل الرئيسية
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print ("الحمد لله البوت اشتغل...")
    app.run_polling()

if __name__ == "__main__":
    main()