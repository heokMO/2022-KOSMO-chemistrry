import cx_Oracle as ora

database = ('chemistrry', 'cherry', 'localhost:1521/xe')
def memberinsert(addr_list):
    conn = ora.connect(database)   #이거 접속하는거 오라클에
    cursor = conn.cursor()         #이게 preparedstatment 그거에 해당하는거
    #num id pwd name email tel addr , date
    sql = "insert into member values(member_seq.nextVal,:1,:2,:3,:4,:5,:6,sysdate)"
    cursor.execute(sql,addr_list)                    #튜플에서 끊어내는 방식이 :
    cursor.close()
    conn.commit()
    conn.close()

# Create your models here.
