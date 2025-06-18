# from src.myproj.db_util import drop_table
# from src.myproj.db_util import create_table
# from src.myproj.db_util import create_table, drop_table
import src.myproj.db_util as db
from src.myproj.db_util import get_connection


def show_main_menu():
    print('[0] 프로그램 종료 [1] 테이블 생성 [2] 테이블 삭제 [3] 테이블 전체 검색 [4] 부서 번호로 검색 [5] 부서 이름으로 검색'
          '[6] 데이터 추가 [7] 데이터 업데이트 [8] 데이터 삭제')
    menu = input('작업하실 번호를 입력하세요. ')
    return menu


def select_want_number():
    vin = []
    with get_connection() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute('select * from dept_ex')
                for row in cursor:
                    vin.append(row[0])
            except Exception as e:
                print(e)
    return vin


def select_want_dname():
    vin = []
    with get_connection() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute('select * from dept_ex')
                for row in cursor:
                    vin.append(row[1])
            except Exception as e:
                print(e)
    return vin


def select_want_loc():
    vin = []
    with get_connection() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute('select * from dept_ex')
                for row in cursor:
                    vin.append(row[2])
            except Exception as e:
                print(e)
    return vin


def create_table_sj(menu):
    if int(menu) != int(menu):
        print('정수만 입력 가능합니다 >>')
    elif int(menu) == int(menu):
        db.create_table()


def select_dept_by_deptno_sj():
    print(select_want_number())
    new = input('검색하고 싶은 부서 번호 입력 : ')
    return db.select_dept_by_deptno(new)


def select_dept_by_dname_sj():
    print(select_want_dname())
    new = input('검색을 원하는 부서 이름을 입력하세요 >>>')
    return db.select_dept_by_dname(new)


def insert_dept_sj():
    print(select_want_number())
    number = input('추가 할 부서 번호를 입력하세요 :')
    print(select_want_dname())
    name = input('추가 할 부서 이름을 입력하세요 :').upper()
    print(select_want_loc())
    loc = input('추가 할 부서 위치를 입력하세요 :').upper()
    return db.insert_dept(number, name, loc)  # 대문자 자동 반영


def dept_ex_update_sj():
    print(select_want_number())
    c_num = input('업데이트 할 부서 번호를 입력하세요 :')
    print(select_want_dname())
    name = input('업데이트 할 부서 이름을 입력하세요 :').upper()
    print(select_want_loc())
    loc = input('업데이트 할 부서 위치를 입력하세요 :').upper()
    print(select_want_number())
    e_num = input('기존에 존재하는 부서 번호를 입력하세요 :')
    print('업데이트가 완료되었습니다. 결과를 다시 확인해주세요. ')
    return db.dept_ex_update(c_num, name, loc, e_num)  # 대문자 자동 반영 !!!


def dept_ex_delete_sj():
    print(select_want_number())
    num = input('삭제 할 부서 번호를  입력해주세요 :')
    print(f'부서번호 {num} 삭제 완료.')
    return db.dept_ex_delete(num)



def main():
    run = True
    while run:
        menu = show_main_menu()
        if menu == '0':
            print('프로그램을 종료합니다 :)')
            run = False
        if menu == '1':
            create_table_sj(menu)
        elif menu == '2':
            db.drop_table()
        elif menu == '3':
            db.select_dept()
        elif menu == '4':
            select_dept_by_deptno_sj()
        elif menu == '5':
            select_dept_by_dname_sj()
        elif menu == '6':
            insert_dept_sj()
        elif menu == '7':
            dept_ex_update_sj()
        elif menu == '8':
            dept_ex_delete_sj()
        else:
            print('메뉴 번호는 0 ~ 8 사이의 정수만 입력 가능합니다.')



if __name__ == '__main__':
    main()



    # db.drop_table()     # dept_ex 테이블 삭제
    # db.create_table()   # dept_ex 테이블 생성
    # # insert
    # db.insert_dept(11, 'IT', '서울')
    # # 전체 검색
    # db.select_dept()
    # # 부서 번호 검색
    # db.select_dept_by_deptno(11)
    # # 부서 정보
    # db.update_dept(11, 'WILL', 'SEOUL')
    # # 검색
    # db.select_dept()
    # # 부서 정보 삭제
    # db.delete_dept(11)
    # # 검색
    # db.select_dept()