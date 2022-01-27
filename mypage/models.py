from django.db import models
import cx_Oracle as ora
# Create your models here.
from conf.settings import oracle_connect_config


def show_myinfo(mem_seq):
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


def info_modify(mem_seq, info):
    conn = ora.connect(oracle_connect_config)
    cursor = conn.cursor()
    sql = """
           update mem set acc_pwd = '{}', nickname = '{}', email= '{}', tel = '{}', univ = '{}', std_id = {}, domi_dong = '{}', room_num = {}  where mem_seq = {}
           """.format(info['acc_pwd'], info['nickname'], info['email'], info['tel'], info['univ'], info['std_id'], info['domi_dong'], info['room_num'], mem_seq)
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()

