import cx_Oracle as ora

# database = ('chemistrry', 'cherry', 'localhost:1521/xe')
database = ('chemistrry/cherry@192.168.0.9/xe')

#list
def help_list():
    conn = ora.connect(database)
    sql = "select p.post_seq, p.title, m.nickname, pc.post_write_time, p.leg_like, p.reply_cnt " \
          "from post p, post_contents pc, mem m " \
          "where m.serialnum = p.serialnum and p.post_seq = pc.post_seq and p.board_type = 1 and p.univ='서울대학교'"
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    cursor.close()
    conn.close()
    return rs

#상세보기
def help_detail():
    conn = ora.connect(database)
    sql = "select p.title, m.nickname, pc.post_write_time, pc.post_content, p.leg_like, p.reply_cnt, pc.post_image " \
          "from post p, post_contents pc, mem m " \
          "where p.post_seq = 38 and m.serialnum = p.serialnum and p.post_seq = pc.post_seq and p.board_type = 1 and p.univ='서울대학교'"
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    cursor.close()
    conn.close()
    return rs


def help_insert():
    conn  = ora.connect(database)
    cursor = conn.cursor()
    sql = "insert into post values(post_seq.nextval,1,'서울대학교',4,'핼프제목더미',0,0)"
    cursor.execute(sql)
    sql = "insert into post_contents values(post_seq.currval,'핼프내용더미',sysdate,'-')"
    cursor.execute(sql)
    sql = "insert into board_reply values(post_seq.currval,reply_seq.nextval,'헬프댓글더미','iammomo',6,sysdate,0)"
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()

def help_update():
    conn  = ora.connect(database)
    cursor = conn.cursor()
    sql = "update post set title = '공지,도와줘제목수정더미' where post_seq = 16"
    cursor.execute(sql)
    sql = "update post_contents set post_content = '공지,도와줘내용수정더미' where post_seq = 16"
    cursor.execute(sql)
    sql = "update post_contents set post_image = '공지,도와줘이미지수정더미' where post_seq = 16"
    cursor.execute(sql)
    conn.commit()
    print("update 성공")
    conn.close()

def help_delete():
    conn = ora.connect(database)
    sql = "delete from post where post_seq = :3"
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()