from django.db import models

# Create your models here.
from conf.settings import database
import cx_Oracle as ora

def reply_list(post_seq):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "select m.nickname, r.reply_comment from reply r, mem m where m.mem_seq = r.mem_seq and r.post_seq = :post_seq order by post_seq desc"
    cursor.execute(sql,post_seq=post_seq)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def reply_cnt(post_seq):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "select count(*) from reply r, mem m where m.mem_seq = r.mem_seq and r.post_seq = :post_seq order by post_seq desc"
    cursor.execute(sql,post_seq=post_seq)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def reply_insert(info):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "insert into reply values(reply_seq.nextval, :1, :2, :3)"
    cursor.execute(sql, info)
    cursor.close()
    conn.commit()
    conn.close()