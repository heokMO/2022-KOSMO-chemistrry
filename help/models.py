from post.models import Post

import cx_Oracle as ora

from conf.settings import database


class Help(Post):
    def post_list(self):
        conn = ora.connect(database)
        cursor = conn.cursor()
        sql = """
            select p.post_seq, p.title, p.post_content, p.written_time, m.nickname, p.view_count 
            from post p, mem m 
            where m.mem_seq = p.mem_seq 
            and board_type = '체리야도와줘'
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def post_insert(self, info):
        super().post_insert('체리야도와줘', info)