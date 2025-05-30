import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os
TOKEN = os.environ.get("TOKEN")

logging.basicConfig(level=logging.INFO)

WORK_DURATION = 50 * 60
SHORT_BREAK = 10 * 60
LONG_BREAK = 30 * 60
CYCLES_BEFORE_LONG_BREAK = 4

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🍅 ببدأ جلسة بومودورو...\nجاهز؟ ✨")
    for cycle in range(1, CYCLES_BEFORE_LONG_BREAK + 1):
        await update.message.reply_text(f"⏱ جلسة {cycle} بدأت! 50 دقيقة شغل 💪")
        await asyncio.sleep(WORK_DURATION)

        if cycle < CYCLES_BEFORE_LONG_BREAK:
            await update.message.reply_text("☕️ استراحة قصيرة 10 دقائق")
            await asyncio.sleep(SHORT_BREAK)
        else:
            await update.message.reply_text("🍽 استراحة طويلة 30 دقيقة! ممتاز 👏")
            await asyncio.sleep(LONG_BREAK)

    await update.message.reply_text("✅ خلصت كل الجلسات! بدك تبدأ من جديد؟ اكتب /start")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()
