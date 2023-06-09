from app.db import get_db

class Mail(object):

    @classmethod
    def get_all(cls):
        db, c = get_db()
        c.execute('select * from mail')
        return c.fetchall()
    
    @classmethod
    def create(cls, email, subject, content):
        db, c = get_db()
        c.execute("insert into mail (email, subject, content) values (%s, %s, %s)", (email, subject, content))
        db.commit()

    @classmethod
    def search(cls, search):
        db, c = get_db()
        search = '%' + search + '%'
        c.execute("select * from mail where email like %s or content like %s or subject like %s", (search, search, search))
        return c.fetchall()