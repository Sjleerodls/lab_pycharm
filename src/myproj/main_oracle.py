import oracledb

user = 'scott'  # DB 접속 사용자 아이디
password = 'tiger'  # DB 접속 비밀번호
dsn = 'localhost/xe'    # domain server name, DB 접속 서버 정보(주소, SID)

if __name__ == '__main__':
    print('oracledb pkg version =', oracledb.__version__)

    # Oracle DB에 접속
    conn = oracledb.connect(user = user, password = password, dsn = dsn)
    """
    dsn만 positional argument이고, 나머지는 *. 
    즉 keyword argument로서 직접 할당해야 함.
    """

    print(conn)
    sql = 'select * from emp'  # DB에서 실행할 SQL 문장. - 끝 부분에 세미콜론을 사용하면 안됨!

    # Cursor 객체 : DB에 SQL 문장을 전송/실행, 그 결과를 처리 할 수 있는 객체.
    cursor = conn.cursor()
    print('cursor =', cursor)

    result = cursor.execute(sql)    # SQL 문장 실행.
    print('result =', result)

    # Cursor 객체는 iterable 타입 -> for-in 반복문에서 사용할 수 있음.
    # row : select 결과에서 1개 행에 저장된 값들로 이루어진 tuple.
    for row in cursor:
        print(row)

    cursor.close()  # 사용이 모두 끝난 커서 객체는 반드시 닫아야 함.
    print('커서 해제 성공')

    # DB 접속 해제.
    conn.close()
    print('DB 접속 해제 성공')