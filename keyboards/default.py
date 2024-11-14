from telebot.types import KeyboardButton,ReplyKeyboardMarkup

def main_menu_uz():
    markup= ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("Mijozlarga👤"),KeyboardButton("Sotuvchilarga🤝"))
    markup.row(KeyboardButton("Platformaga o'tish📲"),KeyboardButton("Tilni o'zgartirish🔄"))
    return markup

def cabinet_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Operator bilan bog'lanish📞"))
    markup.add(KeyboardButton("Kabinetga o'tish💼"))
    markup.add(KeyboardButton("Orqaga ⬅️"))
    return markup

def send_contact(lang):
    markup= ReplyKeyboardMarkup(resize_keyboard=True)
    if lang == "uz":
        markup.add(KeyboardButton("Raqamni jo'natish",request_contact=True))
    elif lang == "eng":
        markup.add(KeyboardButton("Send number",request_contact=True))
    elif lang == "ru":
        markup.add(KeyboardButton("Отправить номер",request_contact=True))
    return markup

def admin_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Foydalanuvchilar soni"))
    markup.add(KeyboardButton("Habar jo'natish"))
    return markup


def main_menu_eng():
    markup= ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("Customers👤"),KeyboardButton("Sellers🤝"))
    markup.row(KeyboardButton("Platforms📲"))
    # markup.row(KeyboardButton("Platforms📲"),KeyboardButton("Change the language🔄"))
    return markup





def main_menu_ru():
    markup= ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("Клиенты👤"),KeyboardButton("Продавцы🤝"))
    markup.row(KeyboardButton("Платформы📲"),KeyboardButton("Изменить язык🔄"))
    return markup
