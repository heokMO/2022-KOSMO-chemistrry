from django.db import models
import cx_Oracle as ora

from conf.settings import orcle_connect_config


def memberInsert(mem_info):
    conn = ora.connect(orcle_connect_config)  # 오라클에 접속
    cursor = conn.cursor()  # preparedStatement
    # addr_list로 넘어온 값들을 순서대로 :1,:2... 자리에 바인딩한다.
    sql = "insert into mem (serialnum, mem_id, mem_pwd, nickname) values ({}, :1, :2, :3)".format(1)
    cursor.execute(sql, mem_info)
    cursor.close()
    conn.commit()
    conn.close()


def idcheck(idx):
    conn = ora.connect(orcle_connect_config)
    cursor = conn.cursor()
    sql = "select count(*) from mem where mem_id=:mem_id"
    cursor.execute(sql, id=idx)
    # fetchone() 단일 커서, 단일 행일 때 사용한다. 상세보기...
    res = cursor.fetchone()
    cursor.close()
    conn.close()
    return res

