from django.db import models

import cx_Oracle as ora

from conf.settings import oracle_connect_config
from member.models import Member


class Post(models.Model):
    def post_insert(self, board_type, mem_seq, info):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        mem = Member()
        univ = mem.get_univ(mem_seq)
        sql = "insert into post values(post_seq.nextval, '{}', '{}', '{}', {}, '{}', sysdate, 0)".format(
            board_type, univ, info['title'], mem_seq, info['post_content'])
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()


    def post_detail(self, post_seq):
        conn = ora.connect(oracle_connect_config)
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
        conn = ora.connect(oracle_connect_config)
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
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        sql = "update post set title = '{}', post_content = '{}' where post_seq = {}".format(
            info['title'], info['content'], post_seq)
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()


    def post_delete(self, post_seq):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        sql = "delete from post where post_seq = {}".format(post_seq)
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()


    def get_board_type(self, post_seq):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        sql = "select board_type from post where post_seq = {}".format(post_seq)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        board_list = {'공지사항': 'notice', '체리야도와줘': 'help'}
        return board_list[result[0]]

    def get_url(self, post_seq):
        dynamic_url = '{}:showpostdetail'.format(Post().get_board_type(post_seq))
        return dynamic_url


