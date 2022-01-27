from post.models import Post
import cx_Oracle as ora
from conf.settings import orcle_connect_config

# 이렇게 Help(Post)를 모듈화한 이유는이 글 목록과 게시글을 등록하는 함수는 공통으로 사용되는 함수이기 떄문에
# 그 함수들을 모아서 모듈화 시킨것이다.
class Help(Post):
    def post_list(self): # 이 함수는 오라클이랑 연동이 시키는 함수
        conn = ora.connect(orcle_connect_config)
        cursor = conn.cursor()
        sql = """
            select p.post_seq, p.title, p.post_content, p.written_time, m.nickname, p.view_count 
            from post p, mem m 
            where m.mem_seq = p.mem_seq 
            and board_type = '체리야도와줘'
        """
        # 타입이 '체리야도와줘'인 게시판에 등록이된 게시물 리스트를 보여주는 쿼리문
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    # 게시물 등록하는 함수
    def post_insert(self, info):
        super().post_insert('체리야도와줘', info)
# super 상위클래스(post)의  post_insert의 함수로 간다
# post_detail, 공통적으로 상속받자