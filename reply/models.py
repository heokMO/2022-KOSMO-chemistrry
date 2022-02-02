from django.db import models

import cx_Oracle as ora

from conf.settings import oracle_connect_config


class Reply(models.Model):
    def write_reply(self, reply_comment, mem_seq, post_seq):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        sql = """
            insert into reply 
            (reply_seq, post_seq, mem_seq, reply_comment) 
            VALUES(REPLY_SEQ.nextval, {post_seq}, {mem_seq}, '{reply_comment}')
        """.format(reply_comment=reply_comment, mem_seq=mem_seq, post_seq=post_seq)
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()


    def show_reply_list(self, post_seq):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        sql = """
            select r.reply_comment, m.nickname, r.written_time, r.reply_seq
            from reply r, mem m
            where r.post_seq = {post_seq}
            and m.mem_seq = r.mem_seq
            order by r.written_time
        """.format(post_seq=post_seq)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result


    def delete_reply(self, reply_seq):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        sql = "delete from reply where reply_seq = {}".format(reply_seq)
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

