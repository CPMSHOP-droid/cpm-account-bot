import os

from telegram import (
    Update,
    LabeledPrice,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    PreCheckoutQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.environ["BOT_TOKEN"]

CHANNEL = "@cpmpremium"
BOT_USERNAME = "CpmAccountShopBot"
SUPPORT_USERNAME = "OTTOCPM"

# Buraya öz Telegram User ID-ni yaz
OWNER_ID = 123456789


def is_owner(update: Update) -> bool:
    return update.effective_user.id == OWNER_ID


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💎 Premium — 500 ⭐", callback_data="show_premium")],
        [InlineKeyboardButton("⭐ Premium Resources — 200 ⭐", callback_data="show_resources")],
        [InlineKeyboardButton("❤️ Support — 10 ⭐", callback_data="show_support")],
    ]

    await update.message.reply_text(
        "🛒 PREMIUM CPM SHOP\n\n"
        "Choose an option:",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def premium_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💳 Buy Premium — 500 ⭐", callback_data="buy_premium")],
        [InlineKeyboardButton("🔙 Back", callback_data="back_menu")],
    ]

    text = (
        "💎 PREMIUM — 500 ⭐\n\n"
        "🚗 All cars purchasable with real money\n"
        "🏁 Mission-exclusive cars\n"
        "👑 King Rank\n"
        "🚘 W16 UNLOCKED\n"
        "👕 All premium clothing UNLOCKED\n"
        "🪙 500K coins + 50M cash\n"
        "🏠 All houses UNLOCKED"
    )

    await update.callback_query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def resources_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(
            "💳 Buy Premium Resources — 200 ⭐",
            callback_data="buy_resources"
        )],
        [InlineKeyboardButton("🔙 Back", callback_data="back_menu")],
    ]

    text = (
        "⭐ PREMIUM RESOURCES — 200 ⭐\n\n"
        "🚗 All cars purchasable with real money\n"
        "👕 Premium clothing"
    )

    await update.callback_query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def support_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💳 Support — 10 ⭐", callback_data="buy_support")],
        [InlineKeyboardButton("🔙 Back", callback_data="back_menu")],
    ]

    text = (
        "❤️ SUPPORT — 10 ⭐\n\n"
        "Support the project and help us continue improving it."
    )

    await update.callback_query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def buy_premium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await context.bot.send_invoice(
        chat_id=query.message.chat_id,
        title="💎 Premium",
        description="Premium account with all listed features.",
        payload="premium_500",
        currency="XTR",
        prices=[LabeledPrice("Premium", 500)],
    )


async def buy_resources(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await context.bot.send_invoice(
        chat_id=query.message.chat_id,
        title="⭐ Premium Resources",
        description="Premium resources and premium content.",
        payload="resources_200",
        currency="XTR",
        prices=[LabeledPrice("Premium Resources", 200)],
    )


async def buy_support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await context.bot.send_invoice(
        chat_id=query.message.chat_id,
        title="❤️ Support",
        description="Support the project.",
        payload="support_10",
        currency="XTR",
        prices=[LabeledPrice("Support", 10)],
    )


async def back_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("💎 Premium — 500 ⭐", callback_data="show_premium")],
        [InlineKeyboardButton("⭐ Premium Resources — 200 ⭐", callback_data="show_resources")],
        [InlineKeyboardButton("❤️ Support — 10 ⭐", callback_data="show_support")],
    ]

    await query.edit_message_text(
        "🛒 PREMIUM CPM SHOP\n\n"
        "Choose an option:",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    if query.data == "show_premium":
        await premium_info(update, context)

    elif query.data == "show_resources":
        await resources_info(update, context)

    elif query.data == "show_support":
        await support_info(update, context)

    elif query.data == "buy_premium":
        await buy_premium(update, context)

    elif query.data == "buy_resources":
        await buy_resources(update, context)

    elif query.data == "buy_support":
        await buy_support(update, context)

    elif query.data == "back_menu":
        await back_menu(update, context)


async def setup_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_owner(update):
        await update.message.reply_text("❌ You are not authorized.")
        return

    keyboard = [
        [
            InlineKeyboardButton(
                "🛒 OPEN SHOP",
                url=f"https://t.me/{BOT_USERNAME}"
            )
        ]
    ]

    text = (
        "🛒 PREMIUM CPM SHOP\n\n"
        "💎 Premium — 500 ⭐\n"
        "⭐ Premium Resources — 200 ⭐\n"
        "❤️ Support — 10 ⭐\n\n"
        "⚡ Fast Delivery\n"
        "🔐 Secure Payment\n"
        "🌍 Worldwide\n\n"
        "👇 Click below to open the shop:"
    )

    await context.bot.send_message(
        chat_id=CHANNEL,
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

    await update.message.reply_text(
        "✅ Shop post successfully published in @cpmpremium."
    )


async def setup_support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_owner(update):
        await update.message.reply_text("❌ You are not authorized.")
        return

    keyboard = [
        [
            InlineKeyboardButton(
                "💬 CONTACT SUPPORT",
                url=f"https://t.me/{SUPPORT_USERNAME}"
            )
        ]
    ]

    text = (
        "❤️ SUPPORT\n\n"
        "Need help with an order, payment, or account?\n\n"
        "Our support team is ready to help you.\n\n"
        "👇 Contact us here:"
    )

    await context.bot.send_message(
        chat_id=CHANNEL,
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

    await update.message.reply_text(
        "✅ Support post successfully published in @cpmpremium."
    )


async def owner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_owner(update):
        await update.message.reply_text("❌ You are not authorized.")
        return

    await update.message.reply_text(
        "👑 Owner access confirmed.\n\n"
        "You have administrator access to the shop bot."
    )


async def precheckout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.pre_checkout_query.answer(ok=True)


async def successful(update: Update, context: ContextTypes.DEFAULT_TYPE):
    payment = update.message.successful_payment
    payload = payment.invoice_payload

    if payload == "premium_500":
        await update.message.reply_text(
            "💎 Premium payment received successfully! ⭐\n\n"
            "Your Premium account is being prepared."
        )

    elif payload == "resources_200":
        await update.message.reply_text(
            "⭐ Premium Resources payment received successfully! ⭐\n\n"
            "Your Premium Resources are being prepared."
        )

    elif payload == "support_10":
        await update.message.reply_text(
            "❤️ Thank you very much for your support! "
            "10 ⭐ received successfully."
        )

    else:
        await update.message.reply_text(
            "⭐ Payment received successfully."
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("setup", setup_channel))
app.add_handler(CommandHandler("setup_support", setup_support))
app.add_handler(CommandHandler("owner", owner))

app.add_handler(CallbackQueryHandler(button_handler))

app.add_handler(PreCheckoutQueryHandler(precheckout))

app.add_handler(
    MessageHandler(filters.SUCCESSFUL_PAYMENT, successful)
)

app.run_polling()
