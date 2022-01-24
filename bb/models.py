import cx_Oracle as ora

# database = ('chemistrry', 'cherry', 'localhost:1521/xe')
database = ('chemistrry/cherry@192.168.0.22/xe')

def examSelect():
    conn = ora.connect(database)
    sql = "select p.post_seq , p.title, pc.post_content, mem.nickname,pc.post_write_time,p.leg_like, p.reply_cnt " \
          "from post p, pos_content pc, mem " \
          "where p.post_seq = 38 and mem.serialnum = p.writer_seq and p.post_seq = pc.post_seq and p.board_type = 0 and p.univ='서울대학교'"
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs)
    cursor.close()
    conn.close()
    return rs

def market_update():
    conn  = ora.connect(database)
    sql = "update post set title = '원하는제목넣어요1' where post_seq = 38"
    cursor = conn.cursor()
    cursor.execute(sql)
    sql = "update pos_content set post_content = '원하는내용넣어요444' where post_seq = 38"
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()

print("--------------------------------------")
market_update()
