from django.db import models
import cx_Oracle as ora
from conf.settings import database

class Post(models.Model):
    def post_insert(self):
        conn = ora.connect(database)
        cursor = conn.cursor()
        sql = "insert into post values(post_seq.nextval, '체리야도와줘', '국민대학교', '제목자리',1, '내용자리', sysdate, 0);'"
        cursor.execute(sql)
        cursor.close()
        conn.close()

    def post_detail(self):
        conn = ora.connect(database)
        cursor = conn.cursor()
        sql = "select p.post_seq, p.title, m.nickname, p.written_time, p.post_content, p.view_count"\
                " from post p, mem m"\
                " where m.mem_seq = p.mem_seq" \
                " and board_type = '체리야도와줘' " \
                " and post_seq = 3"
        cursor.execute(sql)
        rs = cursor.fetchall()
        print(rs)
        cursor.close()
        conn.close()
        return rs


