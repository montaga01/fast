import uvicorn
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler
from telebot.asyncio_helper import ApiGram

# هنا تكتب الرمز السري بتاع البوت
TOKEN = "8184537983:AAFmdN6BTH71K1jAqko46C7P5q9lFr3gldg"

# هنا نجهز تطبيق FastAPI
app = FastAPI()

# هنا نجهز البوت
application = Application.builder().token(TOKEN).build()

# دالة للرد على أمر /start
async def start(update, context):
    await update.message.reply_text("مرحباً بك!")

# إضافة الأمر /start للتعامل معاه
application.add_handler(CommandHandler("start", start))

@app.post(f"/{TOKEN}")
async def webhook_handler(request: Request):
    update = Update.de_json(data=await request.json(), bot=application.bot)
    await application.process_update(update)
    return {"status": "ok"}
