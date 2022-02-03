from django.db import models
import cx_Oracle as ora

from conf.settings import oracle_connect_config


class Member(models.Model):
    def memberInsert(self, mem_info):
        conn = ora.connect(oracle_connect_config)  # 오라클에 접속
        cursor = conn.cursor()  # preparedStatement
        # addr_list로 넘어온 값들을 순서대로 :1,:2... 자리에 바인딩한다.
        sql = "insert into mem (serialnum, mem_id, mem_pwd, nickname) values ({}, :1, :2, :3)".format(1)
        cursor.execute(sql, mem_info)
        cursor.close()
        conn.commit()
        conn.close()

    def idcheck(self, idx):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        sql = "select count(*) from mem where mem_id=:mem_id"
        cursor.execute(sql, id=idx)
        # fetchone() 단일 커서, 단일 행일 때 사용한다. 상세보기...
        res = cursor.fetchone()
        cursor.close()
        conn.close()
        return res

    def login(self, acc_id, acc_pwd):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        sql = """
            select count(*) 
            from mem 
            where ACC_ID='{acc_id}'
            and ACC_PWD='{acc_pwd}'
        """.format(acc_id=acc_id, acc_pwd=acc_pwd)
        cursor.execute(sql)
        # fetchone() 단일 커서, 단일 행일 때 사용한다. 상세보기...
        res = cursor.fetchone()
        cursor.close()
        conn.close()
        return res[0] == 1

    def get_seq(self, user_id):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        sql = """
            select mem_seq
            from mem 
            where ACC_ID='{acc_id}'
        """.format(acc_id=user_id)
        cursor.execute(sql)
        # fetchone() 단일 커서, 단일 행일 때 사용한다. 상세보기...
        res = cursor.fetchone()
        cursor.close()
        conn.close()
        return res[0]

    def get_univ(self, mem_seq):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        sql = "select UNIV from MEM where MEM_SEQ = '{}'".format(mem_seq)
        cursor.execute(sql)
        univ = cursor.fetchone()
        cursor.close()
        conn.close()
        return univ[0]


    def get_nick(self, mem_seq):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        sql = "select NICKNAME from MEM where MEM_SEQ = '{}'".format(mem_seq)
        cursor.execute(sql)
        nick = cursor.fetchone()
        cursor.close()
        conn.close()
        return nick[0]

