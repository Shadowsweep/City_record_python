import pymysql as SQL
try:
    conn = SQL.connect(host = 'localhost',port = 3306,user='root',passwd='2022',database='Places',cursorclass=SQL.cursors.DictCursor)
    smt = conn.cursor()
    pid = int(input("Enter Place Id: "))
    q = "Select * from Record where Placeid={0}".format(pid)
    smt.execute(q)
    row = smt.fetchone()
    if(row):
         print(row['Placeid'],row['Placename'],row['cityname'],row['statename'],row['PlaceDescription'],row['PlaceDistance'])
    else:
        print("No records Found..")
    conn.close()
except Exception as err:
    print("Error:",err)