import os
import pandas as pd

def lihat_data():
    os.system('cls')
    read_data_pengunjung = pd.read_csv("data/daftar_pengunjung.csv",usecols=["No Order","Nama Menu","Jumlah","Total Harga","Tanggal"])#Membaca data sesuai kolom yang diinginkan
    list_data_raw = read_data_pengunjung.values.tolist()#diubah kedalam bentuk list
    no_order_raw,nama_menu,jumlah,total,tanggal= map(list,zip(*list_data_raw))# Zip memisahkan item per index dalam bentuk tuple. Map berfungsi mengubah tuple menjadi list.
    no_order = list(dict.fromkeys(no_order_raw))#Kode ini untuk menghapus item duplicate pada list, cara kerjanya yaitu :  item pada list_order_raw diubah menjadi dictionary key (dictionary key tidak bisa duplicate), lalu diubah menjadi list

    read_data_menu = pd.read_csv("data/data_menu.csv", usecols=["nama_menu","harga"])#Membaca data sesuai kolom yang diinginkan
    list_data_menu = read_data_menu.values.tolist()#diubah ke dalam bentuk list
    menu,harga_menu = map(list,zip(*list_data_menu))# Zip memisahkan item per index dalam bentuk tuple. Map berfungsi mengubah tuple menjadi list.

    menu_jumlah = dict.fromkeys(menu,0) #membuat dictionary untuk menampung jumlah masing-masing menu yang dibeli dan value 0

    for k in range(len(nama_menu)):#perulangan for untuk menghitung jumlah menu yang dibeli secara keseluruhan
        jumlah_total = menu_jumlah[nama_menu[k]] + jumlah[k]
        menu_jumlah[nama_menu[k]] = jumlah_total
    
    #Desain tabel laporan penjualan
    print("-"*66)
    print("|{:^64}|".format("Laporan Penjualan"))
    print("-"*66)
    print("|{:^21}|{:^21}|{:^20}|".format("Tanggal Order","No. Order","Pemasukan"))
    print("-"*66)
    for l in no_order: #For loop untuk mengakses nomor order satu per satu
        jumlah = no_order_raw.count(l)#Menghitung banyak menu yang dibeli
        indeks = no_order_raw.index(l)#Mencari indexnya
        nomor = "{:03d}".format(l)#Format untuk nomor order <000>
        pemasukan = 0 #Menghitung pemasukan yang diberikan setiap pelanggan
        for m in range(jumlah):
            pemasukan += total[indeks + m]#Menambah jumlah pemasukan dari total harga menu
        print("|{:^21}|{:^21}|{:^20}|".format(tanggal[indeks],nomor,pemasukan))#Output
    print("-"*66)
    print("|{:<21}|{:^21}|{:^20}|".format("Banyak Pembeli",len(no_order),sum(total)))#Output banyak pembeli dan total pemasukan dari keseluruhan pelanggan
    print("-"*66)
    print("|{:^4}|{:<15}|{:^12}|{:^17}|{:>12}|".format("No","Nama menu","Harga","Jumlah Terjual","Total Harga"))
    print("-"*66)
    for n in range(len(menu)):#For loop untuk menghitung jumlah menu yang terjual
        Total_harga = harga_menu[n] * menu_jumlah[menu[n]]#Menghitung total pemasukan yang diberikan setiap menu
        print("|{:^4}|{:<15}|{:^12}|{:^17}|{:>12}|".format(n+1,menu[n],harga_menu[n],menu_jumlah[menu[n]],Total_harga))#Output
    print("-"*66)
    print("|{:^51}|{:^12}|".format("Total Penjualan",sum(total)))#output total
    print("-"*66)
    input("Enter untuk kembali")