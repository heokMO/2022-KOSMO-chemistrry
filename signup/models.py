from django.db import models
import cx_Oracle as ora

from conf.settings import oracle_connect_config

# Create your models here.
class Signup(models.Model):
    def signup1(self, mem_info):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        birth = "{}-{}-{}".format(mem_info['yy'], mem_info['mm'], mem_info['dd'])
        mobile = "{}-{}-{}".format(mem_info['mobile'][:3], mem_info['mobile'][3:7], mem_info['mobile'][7:])
        sql = """insert into mem (MEM_SEQ, ACC_ID, ACC_PWD, MEM_NAME, BIRTH, GENDER, EMAIL, TEL)  values 
        (mem_seq.nextval, '{acc_id}', '{pswd1}', '{user_name}', TO_DATE('{birth}','YYYY-MM-DD'), '{gender}','{email}','{mobile}')""".format(
            acc_id=mem_info['acc_id'], pswd1=mem_info['pswd1'], user_name=mem_info['user_name'], birth=birth, gender=mem_info['gender'], email=mem_info['email'], mobile=mobile)
        cursor.execute(sql)
        conn.commit()
        sql = "select last_number from USER_SEQUENCES where sequence_name = 'MEM_SEQ'"
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0] - 1

    def signup2(self, mem_seq, mem_info):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        sql = """update mem set
        NICKNAME = '{nick}', UNIV = '{univ}', STD_ID = {std_id}, DOMI_DONG = '{dormitory}', ROOM_NUM = {room_num}
         where mem_seq = {mem_seq}""".format(
            mem_seq=mem_seq, nick=mem_info['nick'], univ=mem_info['univ'], std_id=mem_info['std_id'], dormitory=mem_info['dormitory'], room_num=mem_info['room_num'])
        cursor.execute(sql)
        conn.commit()
        sql = "select MEM_NAME from mem where MEM_SEQ = {}".format(mem_seq)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0]

    def get_univ_list(self):
        conn = ora.connect(oracle_connect_config)
        cursor = conn.cursor()
        sql = "select uni_name from unilist"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

