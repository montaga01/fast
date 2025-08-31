import os
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# 1️⃣ إعداد التوكن من البيئة
TOKEN = os.environ.get("TELEGRAM_TOKEN")

# 2️⃣ إنشاء تطبيق FastAPI
app = FastAPI()

# 3️⃣ إنشاء البوت باستخدام Application
application = Application.builder().token(TOKEN).build()

# 4️⃣ تعريف أمر /start مع تحقق من وجود الرسالة
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text("مرحباً بك في البوت الدعوي!")
    else:
        print("⚠️ لا يوجد message في التحديث:", update)

# 5️⃣ إضافة الهاندلر
application.add_handler(CommandHandler("start", start))

# 6️⃣ تشغيل البوت وربط الـ webhook عند بدء التطبيق
@app.on_event("startup")
async def on_startup():
    await application.initialize()
    await application.start()
    await application.bot.set_webhook(url=f"https://almontaga-s-project.vercel.app/{TOKEN}")

# 7️⃣ إيقاف البوت وتنظيف الموارد عند إغلاق التطبيق
@app.on_event("shutdown")
async def on_shutdown():
    await application.stop()
    await application.shutdown()

# 8️⃣ استقبال التحديثات من تليجرام ومعالجة الرسائل
@app.post(f"/{TOKEN}")
async def telegram_webhook(request: Request):
    print("✅ الحمد لله الرسالة وصلت")
    data = await request.json()
    print("📦 البيانات المستلمة:", data)

    # تحقق من وجود message و text قبل المعالجة
    if "message" in data and "text" in data["message"]:
        update = Update.de_json(data, application.bot)
        await application.process_update(update)
    else:
        print("⚠️ الرسالة غير قابلة للمعالجة:", data)

    return {"status": "ok"}
