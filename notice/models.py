import cx_Oracle as ora

# database = ('chemistrry', 'cherry', 'localhost:1521/xe')
database = ('chemistrry/cherry@192.168.0.22/xe')


#list
def notice_list():
    conn = ora.connect(database)
    sql = "select p.post_seq, p.title, m.nickname, pc.post_write_time, p.leg_like, p.reply_cnt " \
          "from post p, post_contents pc, mem m " \
          "where m.serialnum = p.serialnum and p.post_seq = pc.post_seq and p.board_type = 0 and p.univ='서울대학교'"
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    cursor.close()
    conn.close()
    return rs

#상세보기
def notice_detail():
    conn = ora.connect(database)
    sql = "select p.title, m.nickname, pc.post_write_time, pc.post_content, p.leg_like, p.reply_cnt, pc.post_image " \
          "from post p, post_contents pc, mem m " \
          "where p.post_seq = 38 and m.serialnum = p.serialnum and p.post_seq = pc.post_seq and p.board_type = 0 and p.univ='서울대학교'"
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    cursor.close()
    conn.close()
    return rs

#insert
def notice_insert():
    conn  = ora.connect(database)
    cursor = conn.cursor()
    sql = "insert into post values(post_seq.nextval,0,'서울대학교',10,'공지사항제목더미',0,0)"
    cursor.execute(sql)
    sql = "insert into post_contents values(post_seq.currval,'공지사항내용더미',sysdate,'-')"
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()

# 수정
def notice_update():
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

def notice_delete():
    conn = ora.connect(database)
    sql = "delete from post where post_seq = :3"
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()