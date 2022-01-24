import cx_Oracle as ora

# database = ('chemistrry', 'cherry', 'localhost:1521/xe')
database = ('chemistrry/cherry@192.168.0.9/xe')

#list
def market_list():
    conn = ora.connect(database)
    sql = "select p.post_seq, p.title, m.nickname, pc.post_write_time, p.leg_like, p.reply_cnt, u.malmuri from post p, post_contents pc, mem m, used_deal u " \
          "where m.serialnum = p.serialnum " \
          "and p.post_seq = pc.post_seq " \
          "and p.post_seq = u.post_seq " \
          "and p.board_type = 3 " \
          "and p.univ='서울대학교'"
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    cursor.close()
    conn.close()
    return rs

#상세보기
def market_details():
    conn = ora.connect(database)
    sql = "select p.title, m.nickname, pc.post_write_time, pc.post_content, ud.price, p.leg_like, p.reply_cnt, pc.post_image, ud.malmuri " \
          "from post p, post_contents pc, mem m, used_deal ud " \
          "where p.post_seq = 19 " \
          "and m.serialnum = p.serialnum " \
          "and p.post_seq = pc.post_seq " \
          "and p.board_type = 3 " \
          "and p.univ='서울대학교' " \
          "and ud.post_seq = p.post_seq"
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    cursor.close()
    conn.close()
    return rs

def market_insert():
    conn  = ora.connect(database)
    cursor = conn.cursor()
    sql = "insert into post values(post_seq.nextval,3,'서울대학교',7,'중고거래제목더미',0,0)"
    cursor.execute(sql)
    sql = "insert into post_contents values(post_seq.currval,'중고거래내용더미',sysdate,'-')"
    cursor.execute(sql)
    sql = "insert into used_deal values(post_seq.currval,1,111111)"
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()

def market_update():
    conn  = ora.connect(database)
    cursor = conn.cursor()
    sql = "update post set title = '중고거래 제목더미' where post_seq = 16"
    cursor.execute(sql)
    sql = "update post_contents set post_content = '중고거래 내용더미' where post_seq = 16"
    cursor.execute(sql)
    sql = "update post_contents set post_image = '중고거래 이미지 더미' where post_seq = 16"
    cursor.execute(sql)
    sql = "update used_deal set price = 100 where post_seq = 16"
    cursor.execute(sql)
    conn.commit()
    print("update 성공")
    conn.close()


def market_delete():
    conn = ora.connect(database)
    sql = "delete from post where post_seq = :3"
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()