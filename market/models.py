from django.db import models
import cx_Oracle as ora
# Create your models here.
database = 'chemistrry/cherry@192.168.0.61/xe'
def postinsert(mem_info, post_contents, post_detail):
    conn = ora.connect(database) #오라클에 접속
    cursor = conn.cursor()  # preparedStatement

    sql = "SELECT post_seq.NEXTVAL FROM dual"
    cursor.execute(sql)
    idx = cursor.fetchone()[0]

    post_type = mem_info[0]
    univ = mem_info[1]
    writer_seq = mem_info[2]
    title = mem_info[3]
    sql = "insert into post values(:id,:type,:univ,:wrtseq,:title,0,0)"
    print(sql)
    cursor.execute(sql, id = idx, type=post_type , univ=univ, wrtseq=writer_seq,title=title) # 튜플에서 데이터를 끌어내는 바인딩 방식

    content = post_contents[0]
    time = post_contents[1]
    file = post_contents[2]
    sql = "insert into pos_content values(:id,:content,:time,:file)"
    print(sql)
    cursor.execute(sql, id = idx, type=post_type , univ=univ, wrtseq=writer_seq,title=title ) # 튜플에서 데이터를 끌어내는 바인딩 방식

    sql = "insert into used_deal values({},{},{})".format(idx,post_detail[0],post_detail[1])
    print(sql)
    cursor.execute(sql) # 튜플에서 데이터를 끌어내는 바인딩 방식

    cursor.close()
    conn.commit()
    conn.close()




