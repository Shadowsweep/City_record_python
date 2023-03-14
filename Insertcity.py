import pymysql as SQL
try:
    conn = SQL.connect(host='localhost',port=3306,user='root',passwd='2022',database ='places')
    smt = conn.cursor()
    pid = input("Enter place id : ")
    pn  = input("Enter Place name: ")
    cn  = input("Enter City name: ")
    sn  = input("Enter State Name: ")
    pdsc  = input("Enter place Description: ")
    pd  = input("Enter place Distance in KM: ")
    q = "insert into Record values({0},'{1}','{2}','{3}','{4}',{5})".format(pid,pn,cn,sn,pdsc,pd)
    print(q)
    smt.execute(q)
    conn.commit()
    print("Data Submitted Successfully")
    conn.close()
except Exception as err:
    print("Error",err)