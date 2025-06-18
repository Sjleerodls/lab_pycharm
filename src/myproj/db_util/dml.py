from oracledb import DatabaseError

from src.myproj.db_util import get_connection

# dept_ex 테이블에 데이터(부서번호, 이름, 위치)를 insert 하는 SQL 문장과 함수를 작성하세요.
dept_insert = '''
insert into dept_ex (deptno, dname, loc) values (int(:num), str(:name), str(:location))
'''

# 오쌤
dept_insert = '''
insert into dept_ex
    values (:dept_no, :dept_name, :location)
'''


def dept_ex_insert(num, name, location):
    with get_connection() as con:
        with con.cursor() as cur:
            try:
                cur.execute(dept_insert, num = num, name = name, location = location)
                con.commit()        # commit 실행
            except Exception as e:
                print(e)


# 오쌤
def insert_dept(dept_no, dept_name, location):
    # step 1. DB 연결
    with get_connection() as conn:
        # step 2. Cursor 객체 생성
        with conn.cursor() as cursor:
            # step 3. SQL 실행
            try:
                # positional argument 방식 -> list, tuple, dict
                # result = cursor.execute(dept_insert, (dept_no, dept_name, location))
                # print('insert result =', result)
                cursor.execute(dept_insert, {'dept_no': dept_no,
                                             'dept_name': dept_name,
                                             'location': location})
                # 가변길이 keyword arg 방식
                # cursor.execute(dept_insert, dept_no = dept_no, dept_name = dept_name, location = location)

                conn.commit()   # DML(insert, update, delete)의 결과를 저장.
            except DatabaseError as e:
                print(e)



# dept_ex 테이블에서 특정 부서 번호의 이름과 위치를 업데이트하는 SQL 문장과 함수를 작성하세요.
dept_update = '''
update dept_ex 
set deptno = :deptno, dname = :name, loc = :location 
where deptno = :num'''


sql_update = '''
update dept_ex 
set dname = :dept_name, loc = :location 
where deptno = :dept_no'''


def dept_ex_update(deptno, dname, loc, number):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(dept_update, deptno = deptno, name = dname, location = loc, num = number )
                conn.commit()
            except Exception as e:
                print(e)


# 오쌤
def update_dept(dept_no, dept_name, location):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(sql_update,
                               dept_no = dept_no,
                               dept_name = dept_name,
                               location = location)
                conn.commit()
                print('update 성공')
            except DatabaseError as e:
                print(e)



# dept_ex 테이블에서 특정 부서 번호의 데이터를 삭제하는 SQL 문장과 함수를 작성하세요.
dept_delete = 'delete from dept_ex where deptno = :deptno'

sql_delete = 'delete from dept_ex where deptno = :dept_no'

def dept_ex_delete(deptno):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(dept_delete, deptno = deptno)
                conn.commit()
            except Exception as e:
                print(e)

# 오쌤
def delete_dept(dept_no):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(sql_delete, dept_no = dept_no)
                conn.commit()
                print('delete 성공')
            except DatabaseError as e:
                print(e)




if __name__ == '__main__':
    # 위에서 선언한 함수들을 테스트하세요.

    # dept_ex_insert(50, 'DATA', 'SEOUL')

    # insert 테스트
    # no = int(input('부서 번호 입력>>> '))
    # name = input('부서 이름 입력>>> ')
    # loc = input('부서 위치 입력>>> ')
    # insert_dept(no, name, loc)

    # dept_ex_update(60, 'ITWILL', 'INCHEON', 50)

    # update 테스트
    # no = int(input('업데이트할 부서 번호 입력>>> '))
    # name = input('업데이트할 부서 이름 입력>>> ')
    # loc = input('업데이트할 부서 위치 입력>>> ')
    # update_dept(no, name, loc)
    # dept_ex_update(no, name, loc, 66)

    # dept_ex_delete(60)

    # delete 테스트
    # no = int(input('삭제할 부서 번호 입력 >>>'))
    # delete_dept(no)

    pass