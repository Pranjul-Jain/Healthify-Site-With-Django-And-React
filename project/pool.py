import pymysql
from django.conf import settings
from pymysql.cursors import DictCursor


def connection():
    try:
        db = pymysql.connect(host="localhost", user='root', port=3306,
                             db=settings.DATABASE_NAME, password=settings.DATABASE_PASSWORD, cursorclass=DictCursor)
        cmd = db.cursor()

        return db, cmd
    except:
        return None
