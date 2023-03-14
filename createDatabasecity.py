import pymysql as SQL
try:
    conn = SQL.connect(host = 'localhost',port = 3306,user='root',passwd='Enter your password')
    smt = conn.cursor()
    q= 'create database Places'
    smt.execute(q)
    conn.commit()
    print("Database created successfully")
    conn.close()
except Exception as err:
    print("Error",err)
