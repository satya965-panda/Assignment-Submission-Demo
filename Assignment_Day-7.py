import mysql.connector as sql           # importing module

# Connecting the local mysql database
database = sql.connect(host = 'localhost', user = 'root', passwd = '1234', database = 'satya', auth_plugin='mysql_native_password')

cur = database.cursor()


cur.execute("update student set name = 'satu' where college = 'KIIT' ")     # Update the record 
cur.execute("select * from student")        # View the table

for i in cur:
    print(i)

cur.close()
database.commit()       # commit changes or save changes.