from post.models import Post

import cx_Oracle as ora

from conf.settings import oracle_connect_config


class Notice(Post):
    def post_list(self):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        sql = """
            select p.post_seq, p.title, m.nickname, p.written_time, p.post_content, p.view_count 
            from post p, mem m 
            where m.mem_seq = p.mem_seq and board_type = '공지사항'
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def post_insert(self, info):
        super().post_insert('공지사항', info)
