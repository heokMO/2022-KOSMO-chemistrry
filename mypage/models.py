from django.db import models
import cx_Oracle as ora
# Create your models here.
from conf.settings import oracle_connect_config

class Mypage(models.Model):
    def show_myinfo(self, mem_seq):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        sql = """
               select mem_name, acc_id, acc_pwd, nickname, birth, gender, email, tel, univ, std_id, domi_dong, room_num from mem where mem_seq = :mem_seq
              """
        cursor.execute(sql, mem_seq=mem_seq)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result


    def post_list(self, mem_seq):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        sql = """
            select p.board_type, p.post_seq, p.title,  p.post_content, p.written_time, p.view_count 
            from post p, mem m 
            where m.mem_seq = p.mem_seq and m.mem_seq =:mem_seq
        """
        cursor.execute(sql, mem_seq=mem_seq)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result


    def info_modify(self, mem_seq, info):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        sql = """
               update mem set 
               acc_pwd = '{}', nickname = '{}', email= '{}', tel = '{}', univ = '{}', std_id = {}, domi_dong = '{}', room_num = {}
               where mem_seq = {}
               """.format(info['acc_pwd'], info['nickname'], info['email'], info['tel'], info['univ'], info['std_id'], info['domi_dong'], info['room_num'], mem_seq)
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()


    def myreply_inpost_list(self, mem_seq):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        sql = """
            select p.board_type, p.post_seq,  p.title,  r.reply_comment, p.WRITTEN_TIME
            from reply r, post p 
            where r.post_seq = p.post_seq
            and r.mem_seq = :mem_seq
        """
        cursor.execute(sql, mem_seq = mem_seq)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result


