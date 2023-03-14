import pymysql as SQL
try:
    conn = SQL.connect(host = 'localhost',port = 3306,user='root',passwd='2022',database='enter your database name')
    smt = conn.cursor()
    q = "create table Record( Placeid int primary key,Placename varchar(30),cityname varchar(30),statename varchar (30),PlaceDescription varchar(200),PlaceDistance varchar(30))"

    smt.execute(q)
    conn.commit()
    print("Table  Records created Successfully")
    conn.close()
except Exception as err:
    print("Error",err)
