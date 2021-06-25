from datetime import date, datetime, timedelta
import mysql.connector

mydb = mysql.connector.connect(
       user='root',
       database='dbrsud'
       )

mycursor = mydb.cursor()
tanggal = datetime.now().date()

####select before ---------------------------------------------------------------------------------
##select_before = ("select * from pelayanan")
##
##mycursor.execute(select_before)
##
##for (no_pelayanan, nik_pasienFK, nipd_dokterFK, gejala, keluhan, solusi, tanggal) in mycursor:
##    print("| {:<2} | {:<10} | {:<10} | {:<20s} | {:<35s} | {:>10s}".format(
##       no_pelayanan, nik_pasienFK, nipd_dokterFK, gejala, keluhan, solusi, tanggal)) 

####insert ========================================================================================
##tambah_pelayanan = ("insert into pelayanan (nik_pasienFK, nipd_dokterFK,"
##                    "gejala, keluhan, solusi, tanggal)"
##                    "values (%s, %s, %s, %s, %s, %s)")
##
##data_pelayanan = ('442210001', '221100001', 'Kulit terasa kering', 'Gatal-gatal',
##                  'Rajin mandi', tanggal)
##
##mycursor.execute(tambah_pelayanan, data_pelayanan)
##mydb.commit()
##
####select after insert ---------------------------------------------------------------------------
##select_after = ("select * from pelayanan")
##
##mycursor.execute(select_after)
##
##for (no_pelayanan, nik_pasienFK, nipd_dokterFK, gejala, keluhan, solusi, tanggal) in mycursor:
##    print("| {:<2} | {:<10} | {:<10} | {:<20s} | {:<35s} | {:>10s}".format(
##       no_pelayanan, nik_pasienFK, nipd_dokterFK, gejala, keluhan, solusi, tanggal)) 

####update ========================================================================================
##update_pelayanan = ("update pelayanan set solusi = 'Lebih menjaga kebersihan' "
##                    "where nik_pasienFK = 442210001")
##
##mycursor.execute(update_pelayanan)
##mydb.commit()
##
##
####select after update ---------------------------------------------------------------------------
##select_after = ("select * from pelayanan")
##
##mycursor.execute(select_after)
##
##for (no_pelayanan, nik_pasienFK, nipd_dokterFK, gejala, keluhan, solusi, tanggal) in mycursor:
##    print("| {:<2} | {:<10} | {:<10} | {:<20s} | {:<35s} | {:>10s}".format(
##       no_pelayanan, nik_pasienFK, nipd_dokterFK, gejala, keluhan, solusi, tanggal)) 

####delete ========================================================================================
##hapus_pelayanan = ("delete from pelayanan where nik_pasienFK = 442210001")
##
##mycursor.execute(hapus_pelayanan)
##mydb.commit()
##
##
####select after delete ---------------------------------------------------------------------------
##select_after = ("select * from pelayanan")
##
##mycursor.execute(select_after)
##
##for (no_pelayanan, nik_pasienFK, nipd_dokterFK, gejala, keluhan, solusi, tanggal) in mycursor:
##    print("| {:<2} | {:<10} | {:<10} | {:<20s} | {:<35s} | {:>10s}".format(
##       no_pelayanan, nik_pasienFK, nipd_dokterFK, gejala, keluhan, solusi, tanggal)) 

##select ========================================================================================
##data nasabah yang melakukan pelayanan antara bulan Februari sampai Juni -----------------------
select_pelayanan = ("select nik_pasienFK, tanggal ,keluhan "
                    "from pelayanan "
                    "where tanggal between '2021-02-01' and '2021-06-31'")

mycursor.execute(select_pelayanan)

for (nik_pasienFK, tanggal, keluhan) in mycursor:
    print('Pasien dengan NIK {} melakukan pelayanan pada {:%d %b %y} dengan keluhan {}'.format(
        nik_pasienFK, tanggal, keluhan))

##-----------------------------------------------------------------------------------------------
mycursor.close()
mydb.close()
