import os
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("TELEGRAM_TOKEN")

app = FastAPI()
application = Application.builder().token(TOKEN).build()

@app.on_event("startup")
async def on_startup():
    application.add_handler(MessageHandler(filters.ALL, start))
    await application.initialize()
    await application.start()
    await application.bot.set_webhook(url=f"https://almontaga-s-project.vercel.app/{TOKEN}")

@app.on_event("shutdown")
async def on_shutdown():
    await application.stop()
    await application.shutdown()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📨 استلمنا رسالتك، وجاري المعالجة...")


@app.post(f"/{TOKEN}")
async def telegram_webhook(request: Request):
    data = await request.json()
    print("📦 البيانات المستلمة:", data)

    # تحويل البيانات إلى كائن Update
    update = Update.de_json(data, application.bot)

    # استخراج chat_id والنص مباشرة
    if update.message and update.message.text:
        chat_id = update.message.chat.id
        user_text = update.message.text

        # إرسال رد مباشر بدون هاندلر
        await application.bot.send_message(chat_id=chat_id, text=f"📨 استلمنا رسالتك: {user_text}")
        application.add_handler(MessageHandler(filters.ALL, start))
    else:
        print("⚠️ لا توجد رسالة قابلة للرد:", data)

    return {"status": "ok"}
