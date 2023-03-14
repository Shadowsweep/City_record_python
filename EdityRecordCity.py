import pymysql as SQL
try:
    conn = SQL.connect(host = 'localhost',port = 3306,user='root',passwd='2022',database='Places',cursorclass=SQL.cursors.DictCursor)
    smt = conn.cursor()
    pid = int(input("Enter Place id : "))
    q = 'Select * from Record where Placeid = {0}'.format(pid)
    smt.execute(q)
    row = smt.fetchone()
    if(row):

        print(" Place Id:",row['Placeid'])
        print("1] place Name: ",row['Placename'])
        print("2] Citname: ",row['cityname'])
        print("3] Statename: ",row['statename'])
        print("4] Place Description: ",row['PlaceDescription'])
        print("5] Place Distance: ",row['PlaceDistance'])
        print("6] Good Bye...")
        f = int(input("Which Field U want to Edit? "))
        if(f==1):
            pn = input("Enter Place name u want : ")
            q= "update   Record  set  placename = '{0}' where Placeid= {1} ".format(pn,pid)
        elif(f==2):
            cn = input("Enter City name: ")
            q = "update Record set  cityname = '{0}' where Placeid ={1}".format(cn,pid)
        elif(f==3):
            sn = input("Enter State name: ")
            q = "update Record set  statename = '{0}' where Placeid ={1}".format(sn,pid)
        elif(f==4):
            pd = input("Enter Place Description: ")
            q = "update Record set  PlaceDescription = '{0}' where Placeid ={1}".format(pd,pid)
        elif(f==5):
            pdis = int(input("Enter Place Distance : "))
            q = "update Record set  PlaceDistance = {0} where Placeid ={1}".format(pdis,pid)
        if(f>=1 and f<=5):
            smt.execute(q)
            conn.commit()
            print("Data Updated Successfully")
    else:
        print("Data not found...")
        conn.close()
except Exception as err:
    print("Error: ",err)
