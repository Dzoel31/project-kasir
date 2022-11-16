import os
import pandas as pd
import prettytable as pt

def table_barang():
    open_file = open("data_barang.csv")
    table_barang = pt.from_csv(open_file)
    print(table_barang)

def menu_edit():
    def save_data(data_barang):
        saved_data = pd.DataFrame(data_barang, columns=[
                             "nama_barang", "jenis_barang", "harga"])
        saved_data.to_csv("data_barang.csv", index=False)

    def curr_data(new_data):
        current_data = pd.read_csv("data_barang.csv")
        data_barang = current_data.values.tolist()

        data_barang.append(new_data)
        save_data(data_barang)

    def add_data():
        nama_barang = input("Masukkan nama barang : ")
        jns_barang = input("Masukkan jenis barang : ")
        harga = int(input("Masukkan harga barang : "))
        new_data = [nama_barang, jns_barang, harga]
        curr_data(new_data)

    def show_data():
        current_data = pd.read_csv("data_barang.csv")
        data_barang = current_data.values.tolist()
        if data_barang == []:
            print("Tidak ada data")
            return "Tidak ada data"
        else:
            table_barang()
        
    def update_harga():
        if show_data() == "Tidak ada data":
            print("Tidak ada data")
            print("Buat data terlebih dahulu!")
        else:
            try:
                current_data = pd.read_csv("data_barang.csv")
                data_barang = current_data.values.tolist()
                pilih = int(input("Pilih data yang mau di perbaharui :"))
                upd_harga = int(input("Masukkan harga baru : "))

                data_barang[pilih][2] = upd_harga
                save_data(data_barang)

            except ValueError:
                print("Input harus Integer!!!")
                update_harga()
                
    def delete_data():
        show_data()
        try:
            current_data = pd.read_csv("data_barang.csv")
            data_barang = current_data.values.tolist()
            pilih = int(input("Pilih data yang mau dihapus : "))
            data_barang.pop(pilih)
            print("Data berhasil dihapus!!")
            save_data(data_barang)
        except ValueError:
            print("Salah inputan")
            delete_data()
    
    os.system('cls')
    print("-"*20)
    print("[1] Buat Data/Tambah Data")
    print("[2] Lihat Data")
    print("[3] Update Harga")
    print("[4] Hapus Data")
    print("[5] Menu sebelumnya")
    print("[0] Exit")
    pilih_menu = int(input("Pilih menu : "))
    if pilih_menu == 1:
        add_data()
    elif pilih_menu == 2:
        show_data()
    elif pilih_menu == 3:
        update_harga()
    elif pilih_menu == 4:
        delete_data()
    elif pilih_menu == 5:
        menu()
    elif pilih_menu == 0:
        exit()
    else:
        print("Salah input!")
        menu_edit()

    check_status = input("Next process?[Y/N] => ")
    if (check_status == "Y") or (check_status == "y"):
        menu_edit()
    else:
        menu()

def pembelian():
    os.system('cls')
    current_data = pd.read_csv("data_barang.csv",usecols=["nama_barang","harga"])
    data_barang = dict(current_data.values.tolist())
    nm_barang = current_data["nama_barang"]
    db_nm_barang = nm_barang.values.tolist()

    barang_beli = []
    total = 0
    ulang = True
    while ulang == True:
        os.system("cls")
        table_barang()
        print(data_barang)

        barang_cust,jumlah_beli = input("Masukkan barang yg dibeli (Namabarang,jumlah beli): ").split(",")

        new_barang = [barang_cust,int(jumlah_beli)]
        barang_beli.append(new_barang)


        tambah =  input("Tambah barang? [y/n] : ")
        if (tambah == "N") or (tambah =="n"):
            break
    
    print("\n{:^61}".format("Struk Belanja"))
    print("-"*61)
    print("|{:^4}|{:^15}|{:^12}|{:^12}|{:^12}|".format("No","Nama Barang","Harga","Jumlah","Total"))
    print("-"*61)

    for k in range(len(barang_beli)):
        if barang_beli[k][0] in db_nm_barang:
            index = db_nm_barang.index(barang_beli[k][0])
            print("|{:^4}|{:^15}|{:^12}|{:^12}|{:^12}|".format(k,barang_beli[k][0],
            data_barang[index][2],
            barang_beli[k][1],
            (barang_beli[k][1]*data_barang[index][2])))
            total += (barang_beli[k][1]*data_barang[index][2])
        else:
            print("Maaf, barang tersebut tidak ada di database kami")
            print("Silahkan masukkan ulang ")
            input()
            pembelian()
    print("-"*61)
    print("|{:^46}|{:^12}|".format("Total Pembayaran",total))
    print("-"*61)
    input("Enter untuk lanjut")
    menu()

def menu():
    os.system('cls')
    print("-"*20)
    print("[1] Edit Data Barang")
    print("[2] Hitung Pembelian")
    print("[0] Exit")
    pilih_menu = int(input("Pilih menu >> "))
    if pilih_menu == 1:
        menu_edit()
    elif pilih_menu == 2:
        pembelian()
    elif pilih_menu == 0:
        exit()
    else:
        print("Input salah! masukkan ulang!")
        menu()

menu()