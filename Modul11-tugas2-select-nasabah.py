from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root', database='dbperbankan')
cursor = cnx.cursor()

query = ("select * from nasabah")

cursor.execute(query)

result = cursor.fetchall() #fetchall untuk menampilkan semua row
                           #fetchone hanya row pertama

for row in result:
    print(row)

