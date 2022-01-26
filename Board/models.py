import cx_Oracle as ora


database = ('chemistrry/cherry@192.168.0.9/xe')

# Create your models here.
#상세보기


class Bb():
    def help_detail(self):
        conn = ora.connect(database)
        sql = "select p.post_seq, p.title, m.nickname, p.written_time, p.post_content, p.view_countfrom post p, mem m" \
              "where m.mem_seq = p.mem_seqand board_type = '체리야도와줘'and post_seq = 3"
        cursor = conn.cursor()
        cursor.execute(sql)
        rs = cursor.fetchall()
        cursor.close()
        conn.close()
        return rs

    def help_insert(self):
        conn  = ora.connect(database)
        cursor = conn.cursor()
        sql = "insert into post values(post_seq.nextval, '공지사항 or 체리야도와줘 넣는자리', '대학교자리', '제목자리',글쓴이시퀀스번호자리, '내용자리', 작성시간자리, 조회수자리)"
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

    def help_update(self):
        conn  = ora.connect(database)
        cursor = conn.cursor()
        sql = "update post set title = '체리야도와줘 제목수정' where post_seq = 3"
        cursor.execute(sql)
        sql = "update post set post_content = '체리야도와줘 내용수정' where post_seq = 3"
        cursor.execute(sql)
        conn.commit()
        print("update 성공")
        conn.close()

    def help_delete(self):
        conn = ora.connect(database)
        sql = "delete from post where post_seq = :3"
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()