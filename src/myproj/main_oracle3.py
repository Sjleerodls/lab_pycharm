# from src.myproj.db_util import drop_table
# from src.myproj.db_util import create_table
# from src.myproj.db_util import create_table, drop_table
import src.myproj.db_util as db

if __name__ == '__main__':
    db.drop_table()     # dept_ex 테이블 삭제
    db.create_table()   # dept_ex 테이블 생성
    # insert
    db.insert_dept(11, 'IT', '서울')
    # 전체 검색
    db.select_dept()
    # 부서 번호 검색
    db.select_dept_by_deptno(11)
    # 부서 정보 업데이트
    db.dept_ex_update(60, '')
    # 검색
    # 부서 정보 삭제
    # 검색