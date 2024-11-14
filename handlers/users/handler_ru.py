from config import GROUP_ID
from loader import db
from telebot.types import Message, ReplyKeyboardRemove
from keyboards.default import *
from keyboards.inline import *


@bot.message_handler(func=lambda message:message.text in ["Клиенты👤","Продавцы🤝"])
def reaction_contact(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"Вы находитесь в разделе {message.text[:-1]}",reply_markup=cabinet_btn_inline_ru())

    bot.delete_message(chat_id, message.id)


