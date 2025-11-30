import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# -------------------------
# SETTINGS
# -------------------------
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

BOOSTED_NUMBERS = ["00", "01", "06", "07", "08", "10", "11", "13", "23", "28"]
BOOST_WEIGHT = 5  # Higher = boosted numbers appear more often

# -------------------------
# FUNCTIONS
# -------------------------
def weighted_random_number():
    normal_pool = [f"{i:02d}" for i in range(33)]  # 00-32
    weighted_pool = normal_pool + BOOSTED_NUMBERS * BOOST_WEIGHT
    return random.choice(weighted_pool)

def generate_numbers():
    numbers = ["00"]  # Always start with 00
    for _ in range(31):  # Generate 31 more numbers
        numbers.append(weighted_random_number())
    return numbers

# -------------------------
# HANDLERS
# -------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    numbers = generate_numbers()
    await update.message.reply_text(" ".join(numbers))

# -------------------------
# RUN BOT
# -------------------------
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()