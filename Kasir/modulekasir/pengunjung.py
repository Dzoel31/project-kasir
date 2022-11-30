import os
import pandas as pd

def lihat_data():
    try:
        os.system('cls')
        read_data_pengunjung = pd.read_csv("data/daftar_pengunjung.csv",usecols=["No Order","Nama Menu","Jumlah","Total Harga","Tanggal"])
        list_data_raw = read_data_pengunjung.values.tolist()
        no_order_raw,nama_menu,jumlah,total,tanggal= map(list,zip(*list_data_raw))
        
        no_order = list(dict.fromkeys(no_order_raw))

        read_data_menu = pd.read_csv("data/data_menu.csv", usecols=["Nama Menu","Harga"])
        list_data_menu = read_data_menu.values.tolist()
        menu,harga_menu = map(list,zip(*list_data_menu))

        menu_jumlah = dict.fromkeys(menu,0) 

        for k in range(len(nama_menu)):
            jumlah_total = menu_jumlah[nama_menu[k]] + jumlah[k]
            menu_jumlah[nama_menu[k]] = jumlah_total
        
        print("-"*66)
        print("|{:^64}|".format("Laporan Penjualan"))
        print("-"*66)
        print("|{:^21}|{:^21}|{:^20}|".format("Tanggal Order","No. Order","Pemasukan"))
        print("-"*66)
        for l in no_order: 
            jumlah = no_order_raw.count(l)
            indeks = no_order_raw.index(l)
            nomor = "{:03d}".format(l)
            pemasukan = 0 
            for m in range(jumlah):
                pemasukan += total[indeks + m]
            print("|{:^21}|{:^21}|{:>20}|".format(tanggal[indeks],nomor,pemasukan))
        print("-"*66)
        print("|{:^21}|{:^21}|{:>20}|".format("Banyak Pembeli",len(no_order),sum(total)))
        print("-"*66)
        print("|{:^4}|{:^15}|{:^12}|{:^17}|{:^12}|".format("No","Nama menu","Harga","Jumlah Terjual","Total Harga"))
        print("-"*66)
        for n in range(len(menu)):
            Total_harga = harga_menu[n] * menu_jumlah[menu[n]]
            print("|{:^4}|{:<15}|{:^12}|{:^17}|{:>12}|".format(n+1,menu[n],harga_menu[n],menu_jumlah[menu[n]],Total_harga))
        print("-"*66)
        print("|{:^51}|{:>12}|".format("Total Penjualan",sum(total)))
        print("-"*66)
        input("Enter untuk kembali")

    except (ValueError):
        input("Belum ada data transaksi! \n Tekan enter untuk lanjut!")
    
    except (FileNotFoundError):
        input("File tidak ditemukan! Periksa kembali alamat atau nama file! \n Tekan enter untuk lanjut!")