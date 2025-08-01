from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random
import os
from dotenv import load_dotenv

# এনভায়রনমেন্ট ভেরিয়েবল লোড করুন
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# বাংলা জোকসের তালিকা
bangla_jokes = [
    "শিক্ষক: তোমার বাবা কি করেন?\nছাত্র: স্যার, তিনি একজন ম্যাজিশিয়ান।\nশিক্ষক: কিভাবে?\nছাত্র: আমার মা বলেন, তিনি টাকা গায়েব করে দেন!",
    # ... অন্যান্য জোকস ...
]

# ইংরেজি জোকসের তালিকা
english_jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    # ... অন্যান্য জোকস ...
]

# /joke কমান্ড হ্যান্ডলার
async def joke_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ... আগের কোড ...

# /start কমান্ড হ্যান্ডলার
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ... আগের কোড ...

# মূল ফাংশন
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("joke", joke_command))
    print("জোকস বট চালু হয়েছে...")
    app.run_polling()

if __name__ == "__main__":
    main()
