from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root', database='dbperbankan')
cursor = cnx.cursor()
tanggal = datetime.now().date()

update_transaksi = ("update transaksi set jumlah = 225000 "
                    "where id_nasabahFK = 11")

cursor.execute(update_transaksi)

cnx.commit() #untuk merubah data pada sql
cursor.close()
cnx.close()
