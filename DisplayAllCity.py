import pymysql as SQL
try:
    conn = SQL.connect(host = 'localhost',port = 3306,user='root',passwd='2022',database='Places',cursorclass=SQL.cursors.DictCursor)
    smt = conn.cursor()
    q = "Select * from Record"
    smt.execute(q)
    records = smt.fetchall()
    if(records):
        for row in records:
            print(row['Placeid'],row['Placename'],row['cityname'],row['statename'],row['PlaceDescription'],row['PlaceDistance'])
    else:
        print("No records Found..")
    conn.close()
except Exception as err:
    print("Error:",err)