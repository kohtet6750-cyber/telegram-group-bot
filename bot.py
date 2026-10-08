import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "မင်္ဂလာပါ 👋\n"
        "Bot အလုပ်လုပ်နေပါပြီ။\n\n"
        "/help - Commands ကြည့်ရန်\n"
        "/hyperlink - Hyperlink mode\n"
        "/mono - Mono mode"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Bot Commands\n\n"
        "/start - Bot စတင်ရန်\n"
        "/help - Help ပြရန်\n"
        "/hyperlink - Hyperlink mode\n"
        "/mono - Mono mode"
    )


async def hyperlink(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔗 Hyperlink mode ဖွင့်ထားပါတယ်။")


async def mono(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔤 Mono mode ဖွင့်ထားပါတယ်။")


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is not set")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("hyperlink", hyperlink))
    app.add_handler(CommandHandler("mono", mono))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
