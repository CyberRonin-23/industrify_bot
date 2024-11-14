from telebot.types import CallbackQuery, ReplyKeyboardRemove
from keyboards.default import *
from keyboards.inline import *
from loader import bot, db


@bot.callback_query_handler(func=lambda call:  "recontact_" in call.data)
def reaction_contact_inline(call: CallbackQuery):
    chat_id = call.message.chat.id
    if "eng" in call.data:
        bot.send_message(chat_id, "Send your number so that our operators can contact you.",
                     reply_markup=send_contact("eng"))
    elif "uz" in call.data:
        bot.send_message(chat_id, "Operatorlar siz bilan bog'lanishlari uchun raqamingizni yuboring.",
                         reply_markup=send_contact("uz"))
    else :
        bot.send_message(chat_id, "Отправьте свой номер, чтобы операторы могли с вами связаться.",
                         reply_markup=send_contact("ru"))
    bot.delete_message(chat_id, call.message.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("recontacted:"))
def handle_recontacted_callback(call: CallbackQuery):
    user_id = call.data.split("|")[1]
    phone_num = call.data.split("|")[2]
    client_username = call.data.split("|")[3]
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=f"""Client's telegram_id: {user_id}
Client's contact: {phone_num}
Client's username: @{client_username}
Operator's username: @{call.from_user.username if call.from_user.username else "No username"}


Status: Has been contacted✅"""
    )

