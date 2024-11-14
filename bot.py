from loader import bot,db
import handlers
from tasks import *

db.create_users()

if __name__ == '__main__':
    print("Bot has started!")
    # initialize_client_base()
    bot.infinity_polling()