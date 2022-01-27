from django.db import models

import cx_Oracle as ora

from conf.settings import database


class Post(models.Model):
    def post_insert(self, board_type, info):
        conn = ora.connect(database)
        cursor = conn.cursor()
        sql = "insert into post values(post_seq.nextval, '{}', '{}', '{}', {}, '{}', sysdate, 0)".format(
            board_type, "국민대학교", info['title'], 1, info['post_content']) #univ, mem_seq
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()


    def post_detail(self, post_seq):
        conn = ora.connect(database)
        cursor = conn.cursor()
        sql = """
        select p.title, m.nickname,  p.post_content, p.written_time, p.view_count
        from post p, mem m
        where m.mem_seq = p.mem_seq
        and post_seq = {}
        """.format(post_seq)

        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result


    def post_update_detail(self, post_seq):
        conn = ora.connect(database)
        cursor = conn.cursor()
        sql = """
        select p.title, m.nickname,  p.post_content
        from post p, mem m
        where m.mem_seq = p.mem_seq
        and post_seq = {}
        """.format(post_seq)

        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result


    def post_update(self, post_seq, info):
        conn = ora.connect(database)
        cursor = conn.cursor()
        sql = "update post set title = '{}', post_content = '{}' where post_seq = {}".format(info['title'], info['content'], post_seq)
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()


    def post_delete(self, post_seq):
        conn = ora.connect(database)
        cursor = conn.cursor()
        sql = "delete from post where post_seq = {}".format(post_seq)
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

