from config import TOKEN
from telebot import TeleBot,custom_filters
from database import DataBase
from telebot.storage import StateMemoryStorage

bot = TeleBot(TOKEN,state_storage=StateMemoryStorage())

bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.ChatFilter())

db = DataBase()

