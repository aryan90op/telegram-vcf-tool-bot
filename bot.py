import logging
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.ext import Dispatcher

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace with your bot's token
TELEGRAM_API_TOKEN = os.getenv(7691719576:AAHuR9ZSK7e6WeuXEof2EtVQ1vhKSgmKCok)

# Function to start the bot
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Send me a file to get started.')

# Function to handle documents sent to the bot
def handle_document(update: Update, context: CallbackContext) -> None:
    file = update.message.document.get_file()
    file.download(f"{file.file_id}.vcf")
    update.message.reply_text('File received and saved as VCF.')

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(7691719576:AAHuR9ZSK7e6WeuXEof2EtVQ1vhKSgmKCok)

    # Get the dispatcher to register handlers
    dispatcher: Dispatcher = updater.dispatcher

    # Register command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Register document handler
    dispatcher.add_handler(MessageHandler(Filters.document, handle_document))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
