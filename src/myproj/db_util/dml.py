from src.myproj.db_util import get_connection

# dept_ex 테이블에 데이터(부서번호, 이름, 위치)를 insert 하는 SQL 문장과 함수를 작성하세요.
dept_insert = '''
insert into dept_ex (deptno, dname, loc) values (:num, :name, :location)
'''

def dept_ex_insert(num, name, location):
    with get_connection() as con:
        with con.cursor() as cur:
            try:
                cur.execute(dept_insert, num = num, name = name, location = location)
                con.commit()        # commit 실행
            except Exception as e:
                print(e)



# dept_ex 테이블에서 특정 부서 번호의 이름과 위치를 업데이트하는 SQL 문장과 함수를 작성하세요.
dept_update = '''
update dept_ex set deptno = :deptno, dname = :name, loc = :location where deptno = :num'''

def dept_ex_update(deptno, dname, loc, number):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(dept_update, deptno = deptno, name = dname, location = loc, num = number )
                conn.commit()
            except Exception as e:
                print(e)



# dept_ex 테이블에서 특정 부서 번호의 데이터를 삭제하는 SQL 문장과 함수를 작성하세요.
dept_delete = 'delete from dept_ex where deptno = :deptno'

def dept_ex_delete(deptno):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(dept_delete, deptno = deptno)
                conn.commit()
            except Exception as e:
                print(e)



if __name__ == '__main__':
    # 위에서 선언한 함수들을 테스트하세요.
    # dept_ex_insert(50, 'DATA', 'SEOUL')

    # dept_ex_update(60, 'ITWILL', 'INCHEON', 50)

    # dept_ex_delete(60)