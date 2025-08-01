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
    "ডাক্তার: আপনার সমস্যা কি?\nরোগী: ডাক্তার সাহেব, আমি খুব ভুলে যাই।\nডাক্তার: কখন থেকে?\nরোগী: কখন থেকে বললাম?",
    "পুলিশ: তোমার নাম কি?\nচোর: আমার নাম তো সবাই জানে।\nপুলিশ: তাহলে তুমি কে?\nচোর: আমি সেই চোর যাকে সবাই চেনে।",
    "স্বামী: আজ আমি তোমাকে একটা চমক দেব।\nস্ত্রী: কি চমক?\nস্বামী: আজ রাতে আমি বাড়ি ফিরব না!",
    "শিক্ষক: তোমার হোমওয়ার্ক কোথায়?\nছাত্র: স্যার, আমার কুকুর খেয়ে ফেলেছে।\nশিক্ষক: তোমার তো কুকুর নেই!\nছাত্র: হ্যাঁ, তাই তো খেতে পারেনি!"
]

# ইংরেজি জোকসের তালিকা
english_jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call fake spaghetti? An impasta!",
    "Why did the math book look so sad? Because it had too many problems.",
    "What do you call a bear with no teeth? A gummy bear!"
]

# /joke কমান্ড হ্যান্ডলার
async def joke_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # কমান্ডের আর্গুমেন্ট চেক করা
    args = context.args
    
    # যদি ভাষা নির্দিষ্ট করা হয়
    if args:
        language = args[0].lower()
        if language in ['bn', 'bangla']:
            joke = random.choice(bangla_jokes)
            await update.message.reply_text(f"🇧🇩 বাংলা জোকস:\n\n{joke}")
            return
        elif language in ['en', 'english']:
            joke = random.choice(english_jokes)
            await update.message.reply_text(f"🇺🇸 English Joke:\n\n{joke}")
            return
    
    # এলোমেলো ভাবে ভাষা নির্বাচন
    language = random.choice(['bangla', 'english'])
    
    if language == 'bangla':
        joke = random.choice(bangla_jokes)
        await update.message.reply_text(f"🇧🇩 বাংলা জোকস:\n\n{joke}")
    else:
        joke = random.choice(english_jokes)
        await update.message.reply_text(f"🇺🇸 English Joke:\n\n{joke}")

# /start কমান্ড হ্যান্ডলার
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 স্বাগতম! আমি র্যান্ডম জোকস বট!\n\n"
        "ব্যবহারবিধি:\n"
        "/joke - এলোমেলো জোকস পাবেন\n"
        "/joke bn - শুধু বাংলা জোকস\n"
        "/joke en - শুধু ইংরেজি জোকস\n\n"
        "প্রতিবার নতুন জোকস পেতে /joke লিখুন!"
    )

# মূল ফাংশন
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("joke", joke_command))
    print("জোকস বট চালু হয়েছে...")
    app.run_polling()

if __name__ == "__main__":
    main()
