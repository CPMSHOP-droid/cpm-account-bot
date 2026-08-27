import os

from telegram import Update, LabeledPrice, InlineKeyboardButton, InlineKeyboardMarkup
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


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💎 Premium — 500 ⭐", callback_data="show_premium")],
        [InlineKeyboardButton("⭐ Premium Resources — 200 ⭐", callback_data="show_resources")],
        [InlineKeyboardButton("❤️ Support — 10 ⭐", callback_data="show_support")],
    ]

    await update.message.reply_text(
        "🛒 Welcome!\n\n"
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
        [InlineKeyboardButton("💳 Buy Premium Resources — 200 ⭐", callback_data="buy_resources")],
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
        [InlineKeyboardButton("❤️ Support — 10 ⭐", callback_data="buy_support")],
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
        currency="XTR
