import os
from telegram import Update, LabeledPrice
from telegram.ext import (
    Application,
    CommandHandler,
    PreCheckoutQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.environ["BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Oyun hesabı üçün ödəniş etmək istəyirsinizsə /pay yazın."
    )

async def pay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_invoice(
        chat_id=update.effective_chat.id,
        title="Oyun hesabı",
        description="Oyun hesabının ödənişi",
        payload="game_account_500",
        currency="XTR",
        prices=[LabeledPrice("500 Stars", 500)],
    )

async def precheckout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.pre_checkout_query.answer(ok=True)

async def successful(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ödəniş qəbul edildi ⭐")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("pay", pay))
app.add_handler(PreCheckoutQueryHandler(precheckout))
app.add_handler(
    MessageHandler(filters.SUCCESSFUL_PAYMENT, successful)
)

app.run_polling()
