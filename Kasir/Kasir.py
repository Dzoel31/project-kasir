import os
from modulekasir import inputdata,pembelian,pengunjung #Import module kasir

def menu():
    os.system('cls') #Membersihkan terminal
    print("Selamat Datang di Menu Restoran Laperpedia")
    print("Apa yang ingin Anda lakukan?")
    print("="*28)
    print("[1] Edit Data Menu Restoran")
    print("[2] Hitung Pembelian")
    print("[3] Lihat Daftar Pengunjung")
    print("[0] Exit")
    print("="*28)
    pilih_menu = int(input("Pilih menu >> "))
    if pilih_menu == 1:
        inputdata.menu_edit()#Menampilkan menu edit
        menu()# Jika proses pada menu sebelumnya selesai, kode ini akan dijalankan. Sehingga akan kembali ke menu utama
    elif pilih_menu == 2:
        pembelian.pembelian()#Menampilkan program untuk menghitung pembelian
        menu()
    elif pilih_menu == 3:
        pengunjung.lihat_data()#Melihat data transaksi
        menu()
    elif pilih_menu == 0:
        exit()#Program berhenti
    else:#Jika salah input maka program akan minta input ulang
        print("Input salah! masukkan ulang!")
        menu()

menu()