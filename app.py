import random
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

def generate_random_number():
    return random.randint(1, 10)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Guess the Number! Try to guess a number from 1 to 10")

def guess_number(update, context):
    guessed_number = int(update.message.text)
    
    if guessed_number > target_number:
        context.bot.send_message(chat_id=update.effective_chat.id, text="The hidden number is less")
    elif guessed_number < target_number:
        context.bot.send_message(chat_id=update.effective_chat.id, text="The hidden number is greater")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Congratulations! You guessed the number!")
    
updater = Updater(token='YOUR_TOKEN', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, guess_number))

def main():
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    target_number = generate_random_number()
    main()