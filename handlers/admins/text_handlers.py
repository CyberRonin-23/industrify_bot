from telebot.types import Message, ReplyKeyboardRemove

from loader import bot, db
from config import ADMINS
from states import CopyAdminState
from keyboards.default import admin_menu


@bot.message_handler(commands=['start'], chat_id=ADMINS)
def reaction_admins_commands(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f'Salom ADMIN', reply_markup=admin_menu())



@bot.message_handler(func=lambda message: message.text == 'Foydalanuvchilar soni', chat_id=ADMINS)
def reaction_count_users(message: Message):
    chat_id = message.chat.id
    users = db.users_count()
    bot.send_message(chat_id, f"Foydalanuvchilar soni {users}")

@bot.message_handler(func=lambda message: message.text == 'Habar jo\'natish', chat_id=ADMINS)
def reaction_count_users(message: Message):
    chat_id = message.chat.id
    bot.set_state(message.from_user.id, CopyAdminState.copy, chat_id)
    bot.send_message(chat_id, "Qanday habar jo'natish kerak?", reply_markup=ReplyKeyboardRemove())


@bot.message_handler(content_types=['photo', 'voice', 'text', 'video', 'document', 'audio'],
                     state=CopyAdminState.copy)
def reaction_copy(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    users = [item[0] for item in db.users_ids()]
    count_users = db.users_count()
    count = 0
    for user in users:
        try:
            bot.copy_message(user, chat_id, message.message_id)
            count += 1
        except:
            bot.send_message(chat_id, f"{user} ga jo'natilmadi!")
    bot.send_message(chat_id, f"{count}/{count_users} ta obunachiga jo'natildi!", reply_markup=admin_menu())
    bot.delete_state(user_id, chat_id)







