import os
import uvicorn
import json
from fastapi import FastAPI, Request
from telegram import Bot

# هنا الكود بياخد الرمز السري بتاع البوت من متغيرات البيئة
TOKEN = os.environ.get("TELEGRAM_TOKEN")

# نجهز التطبيق
app = FastAPI()

# نجهز كائن البوت
bot = Bot(TOKEN)

@app.get("/")
async def get_root():
    return {"status": "ok", "message": "Bot is alive and listening!"}

@app.post(f"/{TOKEN}")
async def webhook_handler(request: Request):
    print("الحمد لله، الرسالة وصلت بنجاح")
    try:
        # نقرأ البيانات من الطلب
        data = await request.json()
        
        # نستخرج الرسالة ونصها
        message_data = data.get("message", {})
        chat_id = message_data.get("chat", {}).get("id")
        text = message_data.get("text", "")
        
        # إذا كانت الرسالة هي "/start"
        if text.lower() == "/start":
            await bot.send_message(chat_id=chat_id, text="مرحباً بك!")
        
        return {"status": "ok"}
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"status": "error", "message": str(e)}
