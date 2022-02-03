from member.models import Member
from post.models import Post

import cx_Oracle as ora

from conf.settings import oracle_connect_config


class Notice(Post):
    def post_list2(self, mem_seq):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        print(mem_seq)
        univ = Member().get_univ(mem_seq)
        sql = """
            select p.post_seq, p.title, m.nickname, p.written_time, p.post_content, p.view_count 
            from post p, mem m 
            where m.mem_seq = p.mem_seq 
            and p.board_type = '공지사항' 
            and p.univ ='{}'
            order by p.post_seq desc
        """.format(univ)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result


    def post_list(self, mem_seq, start_post, last_post):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        print(mem_seq)
        univ = Member().get_univ(mem_seq)
        sql = """
                select b.*
                  from (
                        select a.* , rownum as rnum
                          from (
                                select p.post_seq, p.title, m.nickname, p.written_time, p.post_content, p.view_count 
                                  from post p, mem m 
                                 where m.mem_seq = p.mem_seq 
                                   and p.board_type = '공지사항' 
                                   and p.univ ='{}'
                              order by p.post_seq desc  
                          ) a
                  ) b
                   where rnum >= {} and rnum <= {}
        """.format(univ,start_post,last_post)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result


    def post_insert(self, mem_seq, info):
        super().post_insert('공지사항', mem_seq, info)


    def post_count(self, univ):
        cnt = super().post_count('공지사항', univ)
        return cnt