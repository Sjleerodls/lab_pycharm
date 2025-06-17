import oracledb

user = 'Scott'
password = 'tiger'
dsn = 'localhost/xe'

# __name__의 경우 함수나 클래스에 주로 사용됨.
if __name__ == '__main__':
    # with-as 구문을 사용한 DB 접속, Cursor 사용.
    with oracledb.connect(user = user, password = password, dsn = dsn) as conn:
        # conn.close() 메서드 호출은 with-as가 끝날 때 자동으로 호출됨.
        with conn.cursor() as cursor:
            # cursor.close() 메서드 호출은 with-as가 끝날 때 자동으로 호출됨.
            sql = 'select * from dept'
            cursor.execute(sql)
            for row in cursor:
                print(row)