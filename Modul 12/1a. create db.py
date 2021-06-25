import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root'
    )

mycursor = mydb.cursor()

##create database ============================================================
mycursor.execute("CREATE DATABASE dbrsud")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

mycursor.close()
mydb.close()
