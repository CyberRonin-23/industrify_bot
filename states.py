from telebot.handler_backends import State,StatesGroup

class CopyAdminState(StatesGroup):
    copy = State()