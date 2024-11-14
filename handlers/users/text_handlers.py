from config import GROUP_ID, ADMINS
from loader import bot,db
from telebot.types import Message,ReplyKeyboardRemove
from keyboards.default import *
from keyboards.inline import *
from tasks import update_contact, add_user



    # add_user(user_id,user_name)
    # todo send id to database

@bot.message_handler(func=lambda message: message.text in ["Mijozlarga👤", "Sotuvchilarga🤝"])
def reaction_contact(message:Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Siz {message.text[:-3]} bo'limidasiz!", reply_markup=cabinet_btn_inline())
    bot.delete_message(chat_id,message.id)

@bot.message_handler(func=lambda message:"📲" in message.text)
def reaction_platform(message:Message):
    chat_id = message.chat.id
    user_id  = message.from_user.id
    lang = db.get_lang(user_id)[0]
    if lang == "uz":
        bot.send_message(chat_id,"Amaar uz loyihasining platformalari:",reply_markup=platform_btn())
    elif lang == "ru":
        bot.send_message(chat_id,"Платформы проекта Amaar uz:",reply_markup=platform_btn())
    else:
        bot.send_message(chat_id,"Platforms of the Amaar uz project:",reply_markup=platform_btn())


@bot.message_handler(content_types=['contact'])
def send_info_to_group(message:Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_name = message.from_user.username if message.from_user.username else "No username"
    btn  = InlineKeyboardButton("Contacted✅",callback_data=f"recontacted:|{user_id}|{message.contact.phone_number}|{user_name}")
    markup = InlineKeyboardMarkup()
    markup.add(btn)
    lang = db.get_lang(user_id)[0]
    if lang == 'uz':
        bot.send_message(chat_id,"Iltimos kuting! Operatorlarimiz siz bilan 10 daqiqa ichida bog'lanishadi",reply_markup=main_menu_uz())
    elif lang == "eng":
        bot.send_message(chat_id,"Please wait! Our operators will contact you within 10 minutes",reply_markup=main_menu_eng())
    else:
        bot.send_message(chat_id,"Пожалуйста, подождите! Наши операторы свяжутся с вами в течение 10 минут",reply_markup=main_menu_ru())


    bot.send_message(GROUP_ID,f"""Client's TelegramID: {user_id}
Client's username : @{message.from_user.username if message.from_user.username else "No username"}
Client's contact: +{message.contact.phone_number}
    
    
Status: Has not  been contacted❌""",reply_markup=markup)
    db.insert_contact(message.contact.phone_number,user_id)
    # update_contact(user_id,message.contact.phone_number)



@bot.message_handler(func=lambda message:"🔄" in message.text )
def reaction_platform(message:Message):
    chat_id = message.chat.id
    bot.send_message(chat_id,"Choose the language",reply_markup=language_btn())


