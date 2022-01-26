from django.db import models

# Create your models here.
import cx_Oracle as ora

database = ('chemistrry/cherry@192.168.56.1/xe')
#database = ('chemistrry/cherry@192.168.56.1/xe')


class Help_bb():
    #list
    def help_list(self):
        conn = ora.connect(database)
        sql = "select p.post_seq, p.title, m.nickname, p.written_time, p.post_content, p.view_count from post p, mem m where m.mem_seq = p.mem_seq and board_type = '체리야도와줘'"
        cursor = conn.cursor()
        cursor.execute(sql)
        rs = cursor.fetchall()
        cursor.close()
        conn.close()
        return rs
