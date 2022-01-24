import cx_Oracle as ora

# database = ('chemistrry', 'cherry', 'localhost:1521/xe')
database = ('chemistrry/cherry@192.168.0.22/xe')
def delivery_list():
    conn = ora.connect(database)
    sql = "select p.post_seq, p.title, mem.nickname, pc.post_write_time, p.reply_cnt, mr.open_time, mr.available, " \
          "mr.curr_num, mr.tol_num, mr.store_name " \
          "from post p, pos_content pc, mem, meal_recommend mr" \
          "where mem.serialnum = p.writer_seq and p.post_seq = pc.post_seq and p.board_type = 2 and p.univ='서울대학교'"

def delivery__details():
    conn = ora.connect(database)
    sql = "select p.post_seq, p.title, pc.post_content,mem.nickname, pc.post_write_time, p.reply_cnt,br.reply_comment, mr.open_time, mr.available, mr.curr_num, mr.tol_num, mr.store_name " \
          "from post p, pos_content pc, mem, meal_recommend mr,board_reply br " \
          "where p.post_seq = 2 and mem.serialnum = p.writer_seq and p.post_seq = pc.post_seq and p.board_type = 2 and p.univ='서울대학교'"

    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs)
    cursor.close()
    conn.close()
    return rs