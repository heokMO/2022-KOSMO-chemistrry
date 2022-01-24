import cx_Oracle as ora

# database = ('chemistrry', 'cherry', 'localhost:1521/xe')
database = ('chemistrry/cherry@192.168.0.9/xe')

def delivery_list():
    conn = ora.connect(database)
    sql = "select p.post_seq, p.title, m.nickname, pc.post_write_time, mr.store_name, mr.close_time,mr.available, " \
          "mr.curr_num, mr.tol_num, p.reply_cnt " \
          "from post p, post_contents pc, mem m, meal_recommend mr " \
          "where m.serialnum = p.serialnum " \
          "and p.post_seq = pc.post_seq " \
          "and p.board_type = 2 " \
          "and p.univ='서울대학교'" \
          "and mr.post_seq = p.post_seq"
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    cursor.close()
    conn.close()
    return rs

#상세보기
def delivery_details():
    conn = ora.connect(database)
    sql = "select p.title, m.nickname, pc.post_write_time, pc.post_content, mr.store_name, mr.close_time, mr.available, mr.curr_num, " \
          "mr.tol_num, p.leg_like, p.reply_cnt, pc.post_image " \
          "from post p, post_contents pc, mem m, meal_recommend mr " \
          "where p.post_seq = 2 " \
          "and m.serialnum = p.serialnum " \
          "and p.post_seq = pc.post_seq " \
          "and p.board_type = 2 " \
          "and p.univ='서울대학교' " \
          "and mr.post_seq = p.post_seq"
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs)
    cursor.close()
    conn.close()
    return rs

def delivery_insert():
    conn  = ora.connect(database)
    cursor = conn.cursor()
    sql = "insert into post values(post_seq.nextval,2,'서울대학교',7,'배달제목더미',0,0)"
    cursor.execute(sql)
    sql = "insert into post_contents values(post_seq.currval,'배달내용더미',sysdate,'-')"
    cursor.execute(sql)
    sql = "insert into meal_recommend values(post_seq.currval,sysdate,0,1,4,'배달가게이름더미')"
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()

def delivery_update():
    conn  = ora.connect(database)
    cursor = conn.cursor()
    sql = "update post set title = '1111배달 제목 수정 더미' where post_seq = 47"
    cursor.execute(sql)
    sql = "update post_contents set post_content = '11111배달 내용수정 더미' where post_seq = 47"
    cursor.execute(sql)
    sql = "update post_contents set post_image = '11111배달 이미지 수정 더미' where post_seq = 47"
    cursor.execute(sql)
    sql = "update meal_recommend set available = 1 where post_seq = 47"
    cursor.execute(sql)
    conn.commit()
    print("update 성공")
    conn.close()


def delivery_delete():
    conn = ora.connect(database)
    sql = "delete from post where post_seq = :3"
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()