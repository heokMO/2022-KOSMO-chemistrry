from django.db import models

import cx_Oracle as ora

from conf.settings import orcle_connect_config

# 클래스 안에 있는 함수를 인자 값으로 self를 넣어줘야 한다.
class Post(models.Model):
    def post_insert(self, board_type, info):
        # 인자값으로 board_type, info 받았다
        # 그래서 이 함수가 help model에서 호출되었을 때 실행이 된다
        # board_type, info 을 들고 help model에 간다.
        conn = ora.connect(orcle_connect_config)
        cursor = conn.cursor()
        sql = "insert into post values(post_seq.nextval, '{}', '{}', '{}', {}, '{}', sysdate, 0)".format(
            # 게시글을 등록하는 쿼리문인데
            # 게시판 타입           # 제목       #작성자번호 # 내용
            board_type, "국민대학교", info['title'], 1, info['post_content']) #univ, mem_seq
            # request로 받을 때 딕셔너리 형태로 받는데 info에 title이라는 key값의 벨류가 insert의 4번째 format안으로 들어간다
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()
# 상세보기 페이지
    def post_detail(self, post_seq):
        conn = ora.connect(orcle_connect_config) # 내 오라클 서버와 파이참 서버를 연결 시켜서 conn에 넣어
        cursor = conn.cursor()
        # 오라클과 파이참이 연동되어 있는 상태를 conn이라 하고 그 연결과정에 쿼리의 결과물을 저장하고
        # 있는 메모리 공간 cursor를 커서라는 이름으로 저장한다.
        # 내가 오라클에 직접 쿼리문을 써서 입력하지 않아도 밑에 쿼리문에 맞게 오라클에
        # 파이참에서 오라클로 쿼리문을 보낼 때 중간에 데이터를 저장 하는 곳을 cursor라 하고

        # 상세페이지 창에 보이는 요소에 대한 쿼리문
        sql = """
        select p.title, m.nickname,  p.post_content, p.written_time, p.view_count
        from post p, mem m
        where m.mem_seq = p.mem_seq
        and post_seq = {}
        """.format(post_seq)

        cursor.execute(sql) # cursor에 가지고 있는 데이터를 execute(실행)해라
        result = cursor.fetchone() # cursor에 저장되어 있는 데이터를 단일행으로 하나씩 뽑아서 result에 저장한다.
        cursor.close() # cursor에 저장되어 있는 데이터가 삭제된다.
        conn.close() # cursor에 저장되어 있는 데이터가 삭제된다.
        return result # 결과를 내뱉는다 웩


    def post_update_detail(self, post_seq): #HELP, NOTICE 공통사항 오버라이드 하지 않다
        conn = ora.connect(orcle_connect_config)
        cursor = conn.cursor()
        # 글번호에 해당하는 애를 뽑아와서 해당 글번호의 수정 상세페이지의 창을 보여주는 쿼리문
        sql = """
        select p.title, m.nickname,  p.post_content
        from post p, mem m
        where m.mem_seq = p.mem_seq
        and post_seq = {}
        """.format(post_seq)

        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    def post_update(self, post_seq, info): # post_seq, info 이렇게 두개의 인자값을 가지고 뷰스로 간드아
        conn = ora.connect(orcle_connect_config)
        cursor = conn.cursor()

        sql = "update post set title = " \
              "'{}', post_content = " \
              "'{}' where post_seq = " \
               "{}".format(info['title'], info['content'], post_seq)
        # 제목 내용 해당하는 게시글 번호를 뽑아와서 해당 게시글의 내용을 수정해 주는 쿼리문

        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()


    def post_delete(self, post_seq):
        conn = ora.connect(orcle_connect_config)
        cursor = conn.cursor()
        sql = "delete from post where post_seq = {}".format(post_seq)
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

