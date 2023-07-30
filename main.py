import os
import telebot
from functions import *

bot_token = os.environ['TOKEN']

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Funciono')

@bot.message_handler(content_types=['photo'])
def image_group(message):
    chat_id = message.chat.id

    photo_id = message.photo[-1].file_id
    photo_info = bot.get_file(photo_id)
    file_path = photo_info.file_path
    file_name = f"{chat_id}_img.jpg"
    file = bot.download_file(file_path)

    with open(file_name, "wb") as photo:
        photo.write(file)

    image = backgroud_image(file_name)

    with open(image, "rb") as img:
        bot.send_chat_action(chat_id=chat_id, action='upload_photo')
        bot.send_document(chat_id, img)

    os.remove(image)
    os.remove(file_name)

bot.infinity_polling()