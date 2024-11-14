import psycopg2

class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database = 'industrify',
            user = 'iba',
            host = 'localhost',
            password = '123456'
        )

    def manager(self,sql, *args, commit:bool=False,
                                 fetchone:bool=False,
                                 fetchall:bool=False):

        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit: # if commit == True
                    return db.commit()
                elif fetchone:
                    return cursor.fetchone()
                elif fetchall:
                    return cursor.fetchall()




    def save_user(self, telegram_id,username):
        sql = '''INSERT INTO users(telegram_id,username,language) VALUES(%s,%s,'eng')
        ON CONFLICT DO NOTHING'''
        self.manager(sql, telegram_id,username, commit=True)

    def check_user(self, telegram_id):
        sql = '''SELECT * FROM users WHERE telegram_id=%s'''
        return self.manager(sql, telegram_id, fetchone=True)


    def create_users(self):
        sql = '''CREATE TABLE IF NOT EXISTS users(
            
            telegram_id BIGINT PRIMARY KEY,
            username VARCHAR(30),
            contact VARCHAR(15),
            language VARCHAR(5)
            
        )'''
        self.manager(sql,commit=True)


    def insert_contact(self, contact,telegram_id):
        sql = '''UPDATE users SET contact = %s WHERE telegram_id=%s'''
        self.manager(sql, contact,telegram_id, commit=True)

    def edit_language(self, language,telegram_id):
        sql = '''UPDATE users SET language = %s WHERE telegram_id=%s'''

        self.manager(sql, language,telegram_id, commit=True)

    def users_count(self):
        sql = '''SELECT count(telegram_id) FROM users'''
        return self.manager(sql, fetchone=True)[0]


    def users_ids(self):
        sql = '''SELECT telegram_id FROM users'''
        return self.manager(sql, fetchall=True)

    def get_lang(self,telegram_id):
        sql = '''SELECT language from users where telegram_id=%s'''
        return self.manager(sql,(telegram_id,), fetchone=True)


