import pymysql as SQL
try:
    conn= SQL.connect(host='localhost',port=3306,user='root',passwd='2022',database = 'places',cursorclass=SQL.cursors.DictCursor)
    smt = conn.cursor()
    pid = int(input("Enter Place Id U want to Delete: "))
    q  = 'Select * from Record where placeid = {0}'.format(pid)
    smt.execute(q)
    row = smt.fetchone()
    if(row):
        print(row['Placeid'],row['Placename'],row['cityname'],row['statename'],row['PlaceDescription'],row['PlaceDistance'])
        ch = input("Are U sure U want to delete the record y/n : ")
        if(ch=='y' or ch=='Y'):
            smt.execute('Delete from Record where Placeid = {0}'.format(pid))
            conn.commit()
            print("Record Deleted Successfully") 
    else:
        print("Record Not Found")
    conn.close()
except Exception as err:
    print("Error:",err)

