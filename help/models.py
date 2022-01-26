from django.db import models

import cx_Oracle as ora
from conf.settings import database

def help_list():
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "select p.post_seq, p.title, m.nickname, p.written_time, p.post_content, p.view_count from post p, mem m where m.mem_seq = p.mem_seq and board_type = '체리야도와줘' order by post_seq desc"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def help_insert(**kwargs):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "insert into post values(post_seq.nextval, '체리야도와줘', :univ, :title, :mem_seq, :post_content, sysdate, 0)"
    cursor.execute(sql, univ=kwargs['univ'], title=kwargs['title'], mem_seq=kwargs['mem_seq'], post_content=kwargs['content'])
    cursor.close()
    conn.commit()
    conn.close()


def help_detail(post_seq):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "select p.title, m.nickname, p.written_time, p.post_content, p.view_count from post p ,mem m where p.mem_seq = m.mem_seq and post_seq=:post_seq"
    cursor.execute(sql, post_seq=post_seq)
    result = cursor.fetchone()
    cursor.close()
    conn.commit()
    conn.close()
    return result


def show_post_modify(post_seq):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "select p.title, m.nickname, p.post_content from post p ,mem m where p.mem_seq = m.mem_seq and post_seq=:post_seq"
    cursor.execute(sql, post_seq=post_seq)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


def help_update(info):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "update post set title = :1, post_content = :2 , written_time = sysdate where post_seq = :3"
    cursor.execute(sql, info)
    cursor.close()
    conn.commit()
    conn.close()


def help_delete(post_seq):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "delete post where post_seq={}".format(post_seq)
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()