import os
from modulekasir import inputdata,pembelian,pengunjung

def menu():
    os.system('cls')
    print("Selamat Datang di Menu Restoran Laperpedia")
    print("Apa yang ingin Anda lakukan?")
    print("="*28)
    print("[1] Edit Data Menu Restoran")
    print("[2] Hitung Pembelian")
    print("[3] Lihat Daftar Pengunjung")
    print("[0] Exit")
    print("="*28)
    try : 
        pilih_menu = int(input("Pilih menu >> "))
        if pilih_menu == 1:
            inputdata.menu_edit()
            menu()
        elif pilih_menu == 2:
            pembelian.pembelian()
            menu()
        elif pilih_menu == 3:
            pengunjung.lihat_data()
            menu()
        elif pilih_menu == 0:
            exit()
        else:
            input("Input salah! masukkan ulang!\n Enter untuk mengulang!")
            menu()
    except ValueError:
        input("Input harus integer!\n Enter untuk mengulang!")
        menu()
menu()