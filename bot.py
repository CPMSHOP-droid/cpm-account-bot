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
        "🛒 Xoş gəlmisiniz!\n\n"
        "💎 /full — Full Premium Hesab — 500 ⭐\n"
        "⭐ /premium — Premium Resurslar — 200 ⭐\n"
        "❤️ /support — Support — 10 ⭐"
    )


async def full(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_invoice(
        chat_id=update.effective_chat.id,
        title="💎 Full Premium Hesab",
        description="Full Premium oyun hesabı",
        payload="full_premium_500",
        currency="XTR",
        prices=[LabeledPrice("Full Premium Hesab", 500)],
    )


async def premium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_invoice(
        chat_id=update.effective_chat.id,
        title="⭐ Premium Resurslar",
        description="Premium xüsusiyyətlərlə alına bilən maşınlar, geyimlər və digər resurslar aktivdir.",
        payload="premium_resources_200",
        currency="XTR",
        prices=[LabeledPrice("Premium Resurslar", 200)],
    )


async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_invoice(
        chat_id=update.effective_chat.id,
        title="❤️ Support",
        description="Bot layihəsinə dəstək",
        payload="support_10",
        currency="XTR",
        prices=[LabeledPrice("Support", 10)],
    )


async def precheckout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.pre_checkout_query.answer(ok=True)


async def successful(update: Update, context: ContextTypes.DEFAULT_TYPE):
    payment = update.message.successful_payment
    payload = payment.invoice_payload

    if payload == "full_premium_500":
        await update.message.reply_text(
            "💎 500 ⭐ ödənişiniz uğurla qəbul edildi!\n\n"
            "Full Premium hesabınız hazırlanır."
        )

    elif payload == "premium_resources_200":
        await update.message.reply_text(
            "⭐ 200 ⭐ ödənişiniz uğurla qəbul edildi!\n\n"
            "Premium resurslar hesabınız üçün hazırlanır."
        )

    elif payload == "support_10":
        await update.message.reply_text(
            "❤️ Dəstəyiniz üçün çox sağ olun! 10 ⭐ uğurla qəbul edildi."
        )

    else:
        await update.message.reply_text(
            "⭐ Ödəniş uğurla qəbul edildi."
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("full", full))
app.add_handler(CommandHandler("premium", premium))
app.add_handler(CommandHandler("support", support))

app.add_handler(PreCheckoutQueryHandler(precheckout))
app.add_handler(
    MessageHandler(filters.SUCCESSFUL_PAYMENT, successful)
)

app.run_polling()
