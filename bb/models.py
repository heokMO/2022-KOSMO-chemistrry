import cx_Oracle as ora

# database = ('chemistrry', 'cherry', 'localhost:1521/xe')
database = ('chemistrry/cherry@192.168.0.22/xe')

def examSelect():
    conn  = ora.connect(database)
    sql = "select p.post_seq, p.title, pc.post_content, pc.post_write_time, mem.nickname, " \
          "p.leg_like, p.reply_cnt from post p, pos_content pc, mem where mem.serialnum = p.writer_seq and p.post_seq = pc.post_seq and p.board_type = 1 and p.univ='서울대학교'"

    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs)
    cursor.close()
    conn.close()
    return rs
#     conn = ora.connect(database)   #이거 접속하는거 오라클에
#     cursor = conn.cursor()         #이게 preparedstatment 그거에 해당하는거
#     #num id pwd name email tel addr , date
#     sql = "insert into member values(member_seq.nextVal,:1,:2,:3,:4,:5,:6,sysdate)"
#     cursor.execute(sql,addr_list)                    #튜플에서 끊어내는 방식이 :
#     cursor.close()
#     conn.commit()
#     conn.close()

"""
create table post(                          --게시판글
    post_seq            NUMBER PRIMARY KEY, --게시글 시리얼 넘버
    board_type          NUMBER(5),          --게시판 타입(0:공지사항, 1:도와주세요, 2:배달 3:중고)
    univ                VARCHAR2(50),       --소속대학교
    writer_seq          NUMBER,             --작성자 시리얼넘버
    title               VARCHAR2(50),       -- 제목
    leg_like            NUMBER default 0,   -- 좋아요 수
    reply_cnt           NUMBER default 0    -- 댓글 수 
); 

create table pos_content (                          --내용 게시판
    post_seq            number(10) PRIMARY key,     --게시글 시리얼 넘버
    post_content        long,                       --게시글 내용
    post_write_time     date,                       --게시글 작성시각
    post_image          VARCHAR2(1000)              -- 첨부 파일 명
);

CREATE TABLE mem(                       --회원
    serialnum   number PRIMARY key,     -- 회원 시리얼 넘버
    mem_id      VARCHAR2(20),           -- 회원 id
    mem_pwd     varchar2(20),           -- 회원 pwd
    nickname    varchar2(30),           -- 회원 닉네임
    mem_status  NUMBER                  -- 회원등급(0: 관리자, 1: 생활관장, 2: 기숙사생)
);"""
# Create your models here.
# def memberinsert(addr_list):
#     conn = ora.connect(database)   #이거 접속하는거 오라클에
#     cursor = conn.cursor()         #이게 preparedstatment 그거에 해당하는거
#     #num id pwd name email tel addr , date
#     sql = "insert into member values(member_seq.nextVal,:1,:2,:3,:4,:5,:6,sysdate)"
#     cursor.execute(sql,addr_list)                    #튜플에서 끊어내는 방식이 :
#     cursor.close()
#     conn.commit()
#     conn.close()
print("--------------------------------------")
examSelect()