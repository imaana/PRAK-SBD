from datetime import date, datetime, timedelta
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    database='dbrsud'
    )

mycursor = mydb.cursor()
tanggal = datetime.now().date()

##create table ===============================================================
mycursor.execute("""CREATE TABLE dokter(
nipd_dokter INTEGER PRIMARY KEY,
nama_dokter VARCHAR(40) NOT NULL,
alm_dokter VARCHAR(100) NOT NULL,
spesialisasi VARCHAR(40) NOT NULL
);""")

mycursor.execute("""CREATE TABLE pasien(
nik_pasien INTEGER PRIMARY KEY,
nama_pasien VARCHAR(40) NOT NULL,
alm_pasien VARCHAR(100) NOT NULL,
tgl_lahir DATE NOT NULL default current_timestamp
);""")

mycursor.execute("""CREATE TABLE obat(
no_obat INTEGER PRIMARY KEY,
nama_obat VARCHAR(40) NOT NULL,
jenis_obat VARCHAR(40) NOT NULL,
harga INTEGER NOT NULL
);""")

mycursor.execute("""CREATE TABLE pasien_has_obat(
nik_pasienFK INTEGER REFERENCES pasien(nik_pasien) ON DELETE CASCADE ON UPDATE CASCADE,
no_obatFK INTEGER REFERENCES obat(no_obat) ON DELETE CASCADE ON UPDATE CASCADE
);""")

mycursor.execute("""CREATE TABLE pelayanan(
no_pelayanan SERIAL PRIMARY KEY,
nik_pasienFK INTEGER REFERENCES pasien(nik_pasien) ON DELETE CASCADE ON UPDATE CASCADE,
nipd_dokterFK INTEGER REFERENCES dokter(nipd_dokter) ON DELETE CASCADE ON UPDATE CASCADE,
gejala VARCHAR(255) NOT NULL,
keluhan VARCHAR(255) NOT NULL,
solusi VARCHAR(255) NOT NULL,
tanggal DATE NOT NULL default current_timestamp
);""")

##insert into =================================================================

##dokter ----------------------------------------------------------------------
dokter = ("INSERT INTO dokter(nipd_dokter, nama_dokter, alm_dokter, spesialisasi) "
         "VALUES (%s, %s, %s, %s)")
val_dokter = [
    (112210001, 'Budi Eko', 'Jl. Merak No. 20', 'Spesialis Saraf'),
    (112210002, 'Kartika Fatmasari', 'Jl. Rajawali No. 162', 'Spesialis Penyakit Dalam'),
    (112210003, 'Satria Eka', 'Jl. Garuda No. 45', 'Spesialis Paru')
    ]
mycursor.executemany(dokter, val_dokter)
mydb.commit()

##pasien ---------------------------------------------------------------------
pasien = ("INSERT INTO pasien(nik_pasien, nama_pasien, alm_pasien, tgl_lahir) "
         "VALUES (%s, %s, %s, %s)")
val_pasien = [
    (332210004, 'Ratu Fairuz', 'Jl. Manggis No. 07', '2000-12-01'),
    (332210005, 'Sabilla Rosa', 'Jl. Jeruk No. 222', '2000-02-14'),
    (332210006, 'Ayu Itsnaini', 'Jl. Kelapa No. 109', '2001-03-21')
    ]
mycursor.executemany(pasien, val_pasien)
mydb.commit()

##obat ------------------------------------------------------------------------
obat = ("INSERT INTO obat(no_obat, nama_obat, jenis_obat, harga) "
       "VALUES (%s, %s, %s, %s)")
val_obat = [
    (9961, 'Antihistamin', 'Insomnia', 25000),
    (9962, 'Redacid', 'Gangguan Pencernaan', 37000),
    (9963, 'Neonapacin', 'Gangguan Pernafasan', 55000),
    (9964, 'Exelon', 'Alzheimer', 55000),
    (9965, 'Morfin', 'Pereda Nyeri', 17000),
    (9966, 'Paracetamol', 'Demam', 2500)
    ]
mycursor.executemany(obat, val_obat)
mydb.commit()

##pasien_obat ----------------------------------------------------------------
pasien_obat = ("INSERT INTO pasien_has_obat(nik_pasienFK, no_obatFK) "
              "VALUES (%s, %s)")
val_pasien_obat = [
    (332210004, 9961),
    (332210005, 9962),
    (332210006, 9963),
    (332210004, 9964),
    (332210005, 9965),
    (332210006, 9966)
    ]
mycursor.executemany(pasien_obat, val_pasien_obat)
mydb.commit()

##pelayanan -----------------------------------------------------------------
pelayanan = ("INSERT INTO pelayanan(no_pelayanan, nik_pasienFK, "
            "nipd_dokterFK, keluhan, gejala, solusi, tanggal) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)")
val_pelayanan = [
    (1, 332210004, 112210001, 'Tidak bisa tidur', 'Pusing dan mual',
     'Memperbanyak minum air putih', '2021-02-08'),
    (2, 332210005, 112210002, 'Nyeri di perut', 'Tidak bisa BAB',
     'Makan makanan berserat tinggi', '2021-05-10'),
    (3, 332210006, 112210003, 'Susah bernafas', 'Hidung mampet',
     'Tidur yang cukup', '2021-08-01'),
    (4, 332210004, 112210001, 'Mudah lupa dan stress', 'Gangguan memori',
     'Terapi reminiscence', '2021-05-05'),
    (5, 332210005, 112210002, 'Nyeri dan perineum terasa tertekan',
     'Sakit di perut', 'Terapi relaksasi', '2021-02-11'),
    (6, 332210006, 112210003, 'Sakit tenggorokan dan nyeri', 'Badan terasa panas',
     'Perbanyak minum air hangat', '2021-02-25')
    ]
mycursor.executemany(pelayanan, val_pelayanan)
mydb.commit()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
  
mycursor.close()
mydb.close()
