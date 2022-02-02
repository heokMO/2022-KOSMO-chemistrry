from member.models import Member
from post.models import Post

import cx_Oracle as ora

from conf.settings import oracle_connect_config


class Help(Post):
    def post_list(self, mem_seq):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        print(mem_seq)
        univ = Member().get_univ(mem_seq)
        sql = """
            select p.post_seq, p.title, p.post_content, p.written_time, m.nickname, p.view_count 
            from post p, mem m 
            where m.mem_seq = p.mem_seq 
            and board_type = '체리야도와줘'
            and p.univ ='{}'
            order by p.post_seq desc
        """.format(univ)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def post_insert(self, mem_seq, info):
        super().post_insert('체리야도와줘', mem_seq, info)