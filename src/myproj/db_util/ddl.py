from oracledb import DatabaseError

from src.myproj.db_util.connect import get_connection

# Oracle 21c 버전에서는 create table if not exists table_name,
# drop table if exists table_name 구문을 제공하지 않음.
# Oracle 23ai 버전에서는 if not exists, if exists 문법이 가능.
sql_create_table = '''
create table dept_ex
as select * from dept   
'''

sql_drop_table = 'drop table dept_ex'


def create_table():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(sql_create_table)
                print('테이블 dept_ex가 생성됨.')
            except DatabaseError as e:
                print(e)
            # cursor.close()는 자동 호출
        # conn.close()는 자동 호출


def drop_table():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(sql_drop_table)
                print('테이블 dept_ex가 삭제됨.')
            except DatabaseError as e:
                print(e)


if __name__ == '__main__':
    create_table()
    # drop_table()