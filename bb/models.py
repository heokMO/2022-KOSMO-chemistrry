import cx_Oracle as ora

# database = ('chemistrry', 'cherry', 'localhost:1521/xe')
database = ('chemistrry/cherry@192.168.0.9/xe')

def test_insert():
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
    print("insert 성공성공")
    conn.close()


def test_list():
    conn = ora.connect(database)
    sql = "select p.post_seq , p.title, pc.post_content, mem.nickname,pc.post_write_time,p.leg_like, p.reply_cnt " \
          "from post p, post_contents pc, mem " \
          "where p.post_seq = 38 and mem.serialnum = p.serialnum and p.post_seq = pc.post_seq and p.board_type = 0 and p.univ='서울대학교'"
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs)
    cursor.close()
    conn.close()
    return rs

def test_detail():
    conn = ora.connect(database)
    sql = "select p.post_seq , p.title, pc.post_content, mem.nickname,pc.post_write_time,p.leg_like, p.reply_cnt " \
          "from post p, post_contents pc, mem " \
          "where p.post_seq = 38 and mem.serialnum = p.serialnum and p.post_seq = pc.post_seq and p.board_type = 3 and p.univ='서울대학교' and p.post_seq=17"
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs)
    cursor.close()
    conn.close()
    return rs

def test_update():
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

def test_delete():
    conn  = ora.connect(database)
    sql = "update post set title = '원하는제목넣어요1' where post_seq = 38"
    cursor = conn.cursor()
    cursor.execute(sql)
    sql = "update post_contents set post_content = '원하는내용넣어요444' where post_seq = 38"
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()

print("--------------------------------------")
test_update()









