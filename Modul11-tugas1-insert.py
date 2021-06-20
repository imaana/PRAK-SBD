from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root', database='dbperbankan')
cursor = cnx.cursor()
tanggal = datetime.now().date()

tambah_transaksi = ("insert into transaksi (id_nasabahFK, no_rekeningFK,"
                    "jenis_transaksi, tanggal, jumlah)"
                    "values (%s, %s, %s, %s, %s)")

data_transaksi = ('11', '115', 'kredit', tanggal, '115000')
cursor.execute(tambah_transaksi, data_transaksi)

cnx.commit()
cursor.close()
cnx.close()
