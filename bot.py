import os

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MenuButtonCommands,
)

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

# =========================
# LOAD ENV
# =========================

BOT_TOKEN   = os.environ.get("BOT_TOKEN")
WEBAPP_URL  = os.environ.get("WEBAPP_URL")
SUPPORT_URL = os.environ.get("SUPPORT_URL")


# =========================
# OPEN BUTTON
# =========================

def open_button():
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(text="Join", url=WEBAPP_URL)
    ]])


# =========================
# SUPPORT BUTTON
# =========================

def support_button():
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(text="Support", url=SUPPORT_URL)
    ]])


# =========================
# START COMMAND
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Trade Your Favorite Stocks with the Best Stock Market Trading Platform\n"
        "Experience the Best Trading Platform for US Stocks, Global Stocks, Indices, ETFs, Mutual Funds, IPOs, and NRI Investing."
    )
    await update.message.reply_text(text=text, reply_markup=open_button())


# =========================
# OTHER COMMANDS
# =========================

async def us_stocks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🇺🇸 US Stocks\n\nTrade stocks listed on the world's biggest exchanges\nlike NYSE and NASDAQ with competitive spreads.",
        reply_markup=open_button()
    )

async def global_stocks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌍 Global Stocks\n\nDiversify your portfolio with stocks from global markets\nincluding London, Tokyo, Hong Kong, and more.",
        reply_markup=open_button()
    )

async def indices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Indices\n\nDiversify your exposure with the world's leading indices\nlike the S&P 500, Dow Jones, and Nikkei 225.",
        reply_markup=open_button()
    )

async def etfs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📦 ETFs\n\nFind opportunities with trading in the world's most\npopular exchange-traded funds and baskets.",
        reply_markup=open_button()
    )

async def mutual_funds(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌱 Mutual Funds\n\nInvest in a diversified portfolio managed by the\nworld's most trusted fund managers.",
        reply_markup=open_button()
    )

async def ipo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏛️ IPO\n\nDiscover opportunities with the world's most anticipated\ninitial public offerings before they hit the market.",
        reply_markup=open_button()
    )

async def nri(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✈️ NRI Investing\n\nInvest in global and domestic markets seamlessly\nfrom anywhere in the world as an NRI.",
        reply_markup=open_button()
    )

async def help_and_support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💬 Need help or have a suggestion? Contact support and we'll get\nback to you as soon as possible.",
        reply_markup=support_button()
    )


# =========================
# SETUP MENU COMMANDS
# =========================

async def setup_commands(app):
    commands = [
        ("start",            "Start Bot"),
        ("us_stocks",        "US Stocks"),
        ("global_stocks",    "Global Stocks"),
        ("indices",          "Indices"),
        ("etfs",             "ETFs"),
        ("mutual_funds",     "Mutual Funds"),
        ("ipo",              "IPO"),
        ("nri",              "NRI Investing"),
        ("help_and_support", "Help & Support"),
    ]
    await app.bot.set_my_commands(commands)
    await app.bot.set_chat_menu_button(menu_button=MenuButtonCommands())


async def post_init(app):
    await setup_commands(app)


# =========================
# CREATE APP
# =========================

app = (
    Application.builder()
    .token(BOT_TOKEN)
    .post_init(post_init)
    .build()
)

app.add_handler(CommandHandler("start",            start))
app.add_handler(CommandHandler("us_stocks",        us_stocks))
app.add_handler(CommandHandler("global_stocks",    global_stocks))
app.add_handler(CommandHandler("indices",          indices))
app.add_handler(CommandHandler("etfs",             etfs))
app.add_handler(CommandHandler("mutual_funds",     mutual_funds))
app.add_handler(CommandHandler("ipo",              ipo))
app.add_handler(CommandHandler("nri",              nri))
app.add_handler(CommandHandler("help_and_support", help_and_support))


# =========================
# START BOT
# =========================

print("✅ Stocks Bot Running...")
app.run_polling()