from app.db import get_db

class Mail(object):

    @classmethod
    def get_all(cls):
        db, c = get_db()
        c.execute('select * from mail')
        return c.fetchall()