# from .connect import get_connection     # connect 모듈 안의 get_connection 함수를 불러옴.
# from .connect import close_connection
from src.myproj.db_util.connect import get_connection, close_connection # 절대경로 import
from src.myproj.db_util.ddl import create_table, drop_table
from src.myproj.db_util.dql import select_dept, select_dept_by_deptno, select_dept_by_dname
from src.myproj.db_util.dml import insert_dept, dept_ex_update, dept_ex_delete