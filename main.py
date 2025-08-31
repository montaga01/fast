import os
import uvicorn
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler

# هنا الكود بياخد الرمز السري بتاع البوت من متغيرات البيئة في Vercel
TOKEN = os.environ.get("TELEGRAM_TOKEN")

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
