# Nama  : Sayid Rafi A'thaya
# NIM   : 2409116036
print("--------------------------------------")
print("-----------PENGISIAN BENSIN-----------")
print("----------Sayid Rafi A'thaya----------")
print("--------Prodi Sistem Informasi--------")
print("--------------------------------------")

from prettytable import PrettyTable 
#PrettyTable = membuat tabel
#prettytable = menampilkan tabel

tabel = PrettyTable()
tabel.field_names = ["Nomor", "Nama Bensin", "Harga Bensin (Per Liter)"]

#MENAMBAHKAN BENSIN KE DAFTAR
def bensin(nomor, nama_bensin, harga_bensin):
    tabel.add_row([nomor, nama_bensin, harga_bensin])

#DATABASE BENSIN
bensin("1", "Pertalite", "10.000")
bensin("2", "Pertamax", "12.400")
bensin("3", "Pertmax Turbo", "13.550")
bensin("4", "Dexlite", "13.000")
bensin("5", "Pertamina Dex", "13.450")
bensin("6","Bio Solar", "6.800")


#ADMIN/PEMBELI
def login():
    while True:
        print("Selamat Datang di SPBU Samarinda!")
        print("[1]. Admin")
        print("[2]. Pembayar")
        pilihan = input("Silakan Pilih Mode Login : ")
        if pilihan == "1":
            admin()
        elif pilihan == "2":
            pembayar()
            break
        else:
            print("Invalid! , silakan coba kembali!")
            return login()

#LOGIN SEBAGAI ADMIN
def admin():
    while True:
        print("Selamat Datang Admin!")
        print("[1]. Tambah Bensin")
        print("[2]. Habisin Bensin")
        print("[3]. Lihat Bensin")
        print("[4]. Perbarui Bensin")
        print("[5]. Exit/Kembali ke Mode Login")
        opsi = input("Silakan Pilih Opsi Yang diinginkan : ")
        if opsi == "1":
            tambahbensin()
        elif opsi == "2":
            habisinbensin()
        elif opsi == "3":
            lihatbensin()
        elif opsi == "4":
            perbaruibensin()
        elif opsi == "5":
            opsi_login = input ("Apakah anda ingin Exit atau Kembali ke mode login? (Exit/Kembali) : ").capitalize()
            if opsi_login == "Exit":
                print("Terimakasih! Sampai Jumpa Lagi!")
                exit()
            elif opsi_login == "Kembali":
                login()
        else:
            print("Opsi Invalid, silakan coba lagi")

#TAMBAH BENSIN
def tambahbensin():
    while True:
        nomor = input("Input Nomor Bensin: ")
        nama_bensin = input("Input Nama Bensin: ")
        harga_bensin = input("Input Harga Bensin: ")
        bensin(nomor, nama_bensin, harga_bensin)
        print(f"Nomor Bensin [{nomor}] dengan nama [{nama_bensin}] Berhasil Ditambahkan seharga [Rp.{harga_bensin}]")
        pilihan = input("Apakah Ingin menambahkan bensin lagi? (y/n): ")
        if pilihan == "n":
            break

#HABISIN BENSIN
def habisinbensin():
    while True:
        lihatbensin()
        nomor = input("Masukan Nomor Bensin yang ingin dihabiskan : ")

        for row in tabel._rows:
            if row[0] == nomor:
                tabel.del_row(tabel.rows.index(row))
        print(f"Nomor Bensin {nomor} dengan Nama Bensin telah dihabiskan")
        pilihan = input("Apakah Ingin menghabsikan bensin lagi? (y/n): ")
        if pilihan == "n":
            break

#LIHAT BENSIN
def lihatbensin():
    print(tabel)

#PERBARUI BENSIN
def perbaruibensin():
    lihatbensin()
    nomor = input("Input Nomor Bensin awal : ")
    ubah_bensin_harga = input("Pilih yang akan perbarui (Nama/Harga) : ").capitalize()
    nilai_baru = input(f"Input {ubah_bensin_harga} baru : ")

    for row in tabel._rows:
        if row[0] == nomor:
            index = tabel._rows.index(row)
            if ubah_bensin_harga == "Nama":
                tabel._rows[index][1] = nilai_baru
            elif ubah_bensin_harga == "Harga":
                tabel.rows[index][2] = (nilai_baru)
            else:
                print ("Data Inalid")
                return perbaruibensin()
    print(f"Bensin dengan Nomor {nomor} telah diperbarui.")

#LOGIN SEBAGAI PEMBAYAR
def pembayar():
    print( "Selamat Datang Pembayar!")
    nama_pembayar = input("Nama Anda : ")
    print(f"Halo Selamat datang {nama_pembayar} di SPBU Samarinda!")
    
    while True:
        lihatbensin()
        while True:
            nomor = input("Input Nomor Bensin yang ingin dibayar : ")
            cari = False  
            for row in tabel._rows:
                if row[0] == nomor:
                    cari = True
                    kuantitas = int(input("Input Berapa Bensin yang anda inginkan : "))
                    harga_bensin = float(row[2].replace(".", ""))  
                    total_harga = kuantitas * harga_bensin
                    print(f"Anda telah membeli {kuantitas} {row[1]} seharga Rp. ",total_harga) 
            if not cari:
                print("Nomor Bensin Invalid. Silakan coba lagi.")

login()