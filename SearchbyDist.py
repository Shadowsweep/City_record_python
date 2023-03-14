import pymysql as SQL
try:
    conn = SQL.connect(host = 'localhost',port = 3306,user='root',passwd='2022',database='Places',cursorclass=SQL.cursors.DictCursor)
    smt = conn.cursor()
    min = int(input("Enter Min Dist. in Km: "))
    max = int(input("Enter Max Dist in Km: "))
    q = "Select * from Record where PlaceDistance between {0} and {1}".format(min,max)
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