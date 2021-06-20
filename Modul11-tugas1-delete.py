from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root', database='dbperbankan')
cursor = cnx.cursor()
tanggal = datetime.now().date()

hapus_transaksi = ("delete from transaksi where jumlah = 225000")

cursor.execute(hapus_transaksi)

cnx.commit()
cursor.close()
cnx.close()
