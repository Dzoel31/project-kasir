import os
import pandas as pd
from modulekasir.inputdata import read_data_menu,getpaths
from modulekasir.pengunjung import read_data_pengunjung

def jam():
    now = pd.Timestamp.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")
    return current_time

def transaksi(pembayaran,total_bayar):
    if pembayaran < total_bayar:
        print("Uang anda tidak cukup")
        pembayaran = int(input("Jumlah bayar : "))
        transaksi(pembayaran,total_bayar)
    elif pembayaran > total_bayar:
        kembalian = pembayaran - total_bayar
        print(f"Kembalian anda Rp.{kembalian}")
        print("Terima Kasih Sudah Berkunjung")
    else :
        print("Terima Kasih Sudah Berkunjung")

def pembelian():
    try :
        tanggal = jam()
        datamenu = read_data_menu()
        data_pengunjung = read_data_pengunjung()
        daftar_no_order = data_pengunjung.no_order

        menu_beli = [] 
        jumlah_beli = [] 
        nomor_order = len(daftar_no_order) 
        total_bayar = 0 
        
        status = "Y"
        while status == "Y": 
            os.system("cls")
            
            print("-"*54)
            print("|{:^4}|{:^15}|{:^15}|{:^15}|".format("No", "Nama Menu", "Jenis Menu", "Harga"))
            print("-"*54)
            for i in range(len(datamenu.data_menu)):
                print("|{:^4}|{:<15}|{:^15}|{:>15}|".format(i,datamenu.nama_menu[i],datamenu.jenis_menu[i],datamenu.harga[i]))
            print("-"*54)
            menu,jumlah = input("Masukkan menu yg dibeli dengan format (NamaMenu,jumlah beli): ").split(",")
            if menu in datamenu.nama_menu: 
                menu_beli.append(menu) 
                jumlah_beli.append(int(jumlah)) 
                tambah =  input("Tambah menu? [y/n] : ")
                if (tambah == "Y") or (tambah =="y"): 
                    status = "Y"
                else:
                    status = "N"
            else: 
                print("Maaf, Menu tersebut tidak tersedia di restoran kami")
                print("Silahkan masukkan ulang ")
                input()
                pembelian() 
        
        menu_beli2 = list(dict.fromkeys(menu_beli))
        menu_jumlah = dict.fromkeys(menu_beli,0)
        
        for h in range(len(menu_beli)): 
            banyak = menu_jumlah[menu_beli[h]] + jumlah_beli[h]
            menu_jumlah[menu_beli[h]] = banyak
        
        list_pembelian_total = []
        nomor_order += 1 
        
        print("\n{:^61}".format("Struk Belanja"))
        print("-"*61)
        print("|{:^4}|{:^15}|{:^12}|{:^12}|{:^12}|".format("No","Nama Menu","Harga","Jumlah","Total"))
        print("-"*61)
        for k in range(len(menu_beli2)):
            index = datamenu.nama_menu.index(menu_beli2[k])
            total_harga = menu_jumlah[menu_beli2[k]] * datamenu.harga[index]
            total_bayar += total_harga 
            print("|{:^4}|{:<15}|{:^12}|{:^12}|{:>12}|".format(k,menu_beli2[k],datamenu.harga[index],menu_jumlah[menu_beli2[k]],total_harga))

            list_pembelian = [nomor_order,menu_beli2[k],datamenu.harga[index],menu_jumlah[menu_beli2[k]],total_harga,tanggal]
            list_pembelian_total.append(list_pembelian) 
        print("-"*61)
        print("|{:^46}|{:>12}|".format("Total Pembayaran",total_bayar))
        print("-"*61)
        pembayaran = int(input("Jumlah bayar : "))
        transaksi(pembayaran,total_bayar)
        save_data_pengunjung(list_pembelian_total) 
        input("Enter untuk lanjut")

    except ValueError: 
        input("Tidak ada data \n press enter")
    
    except FileNotFoundError:
        input("File tidak ditemukan! Periksa Relative Path file! \n press enter")
        
def save_data_pengunjung(list_pembelian_total):
    path = getpaths()
    list_data_pengunjung = read_data_pengunjung()
    data = list_data_pengunjung.list_data

    data.extend(list_pembelian_total) 

    saved_data = pd.DataFrame(data, columns=["No Order","Nama Menu","Harga","Jumlah","Total Harga","Tanggal"])
    saved_data.to_csv(f"{path}\\daftar_pengunjung.csv",index=False)