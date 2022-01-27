from post.models import Post

import cx_Oracle as ora

from conf.settings import database


def post_list(mem_seq):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = """
        select p.board_type, p.post_seq, p.title,  p.post_content, p.written_time, p.view_count 
        from post p, mem m 
        where m.mem_seq = p.mem_seq and m.mem_seq =:mem_seq
    """
    cursor.execute(sql, mem_seq = mem_seq)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def myreply_inpost_list(mem_seq):
    conn = ora.connect(database)
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


