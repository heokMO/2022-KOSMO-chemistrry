from member.models import Member
from post.models import Post

import cx_Oracle as ora

from conf.settings import oracle_connect_config


class Notice(Post):
    def post_list(self, mem_seq):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
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

    def post_insert(self, mem_seq, info):
        super().post_insert('공지사항', mem_seq, info)

    def post_search(self, mem_seq, target):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        univ = Member().get_univ(mem_seq)
        targets = target.split()
        if len(targets) == 1:
            sentence = '%' + targets[0] + '%'
        elif len(targets) == 0:
            return self.post_list(mem_seq)
        else:
            sentence = '%' + targets[0] + '%'
            for t in targets[1:]:
                sentence += ' | %' + t + '%'
        sql = """
            select p.post_seq, p.title, m.nickname, p.written_time, p.post_content, p.view_count 
            from post p, mem m 
            where m.mem_seq = p.mem_seq 
            and p.board_type = '공지사항' 
            and p.univ ='{univ}'
            and( contains(TITLE,'{sentence}') > 0
            or contains(POST_CONTENT, '{sentence}') > 0
            )
            order by p.post_seq desc
        """.format(univ=univ, sentence=sentence)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
