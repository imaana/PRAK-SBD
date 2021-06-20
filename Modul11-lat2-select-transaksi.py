from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root', database='dbperbankan')
cursor = cnx.cursor()

query = ("select id_nasabahFK, jenis_transaksi, tanggal, jumlah "
         "from transaksi where year(tanggal) = '2009'")

cursor.execute(query)

for (id_nasabahFK, jenis_transaksi, tanggal, jumlah) in cursor:
    print('nasabah dengan ID {} melakukan transaksi {} pada {:%d %b %y} sejumlah {}'.format(
        id_nasabahFK, jenis_transaksi, tanggal, jumlah))

cursor.close()
cnx.close()
