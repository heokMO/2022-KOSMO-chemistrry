from django.db import models
import cx_Oracle as ora
# Create your models here.
database='chemistrry/1234@192.168.56.1/xe'
def postinsert():
    #오라클 접속
    conn = ora.connect(database)
    #prepareled statesment
    cursor = conn.cursor()
    print('conn =>',cursor)
    # num,id,pwd,name,email,tel,addr,mdate
    # :1,:2,:3,:4,:5,:6, 이게 무슨 방법 이라고? 받은 리스트를 하나씩 뽑아내는 바인딩 방식
    sql = "insert into member values(member_seq.nextVal,:1,:2,:3,:4,:5,:6,sysdate)"
    #맵핑후 오라클 쿼리로 전송
    cursor.execute(sql,addr_list)
    cursor.close()
    conn.commit()
    conn.close()