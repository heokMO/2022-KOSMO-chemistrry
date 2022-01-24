import cx_Oracle as ora

# database = ('chemistrry', 'cherry', 'localhost:1521/xe')
database = ('chemistrry/cherry@192.168.0.9/xe')
from django.db import models


# Create your models here.


#상세보기
def reply():
    conn = ora.connect(database)
    sql = "select * from board_reply"

    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    cursor.close()
    conn.close()
    return rs
