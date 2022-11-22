import os
import pandas as pd

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
        nama_barang,jenis_barang,harga = map(list,zip(*data_barang))
        print("-"*54)
        print("|{:^4}|{:^15}|{:^15}|{:^15}|".format(
            "No", "Nama Barang", "Jenis Barang", "Harga"))
        print("-"*54)
        for i in range(len(data_barang)):
            print("|{:^4}|{:^15}|{:^15}|{:^15}|".format(i,nama_barang[i],jenis_barang[i],harga[i]))
        print("-"*54)
    
def update_harga():
    if show_data() == "Tidak ada data":
        print("Tidak ada data")
        print("Buat data terlebih dahulu!")
    else:
        try:
            current_data = pd.read_csv("data_barang.csv")
            data_barang = current_data.values.tolist()
            pilih = int(input("Pilih data yang mau di perbaharui : "))
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

def menu_edit():
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
    current_data = pd.read_csv("data_barang.csv")
    data_barang = current_data.values.tolist()
    nama_barang,jenis_barang,harga = map(list,zip(*data_barang))
    barang_beli = []
    jumlah_beli = []
    total = 0
    ulang = 1
    while ulang == 1:
        os.system("cls")
        print("-"*54)
        print("|{:^4}|{:^15}|{:^15}|{:^15}|".format(
                    "No", "Nama Barang", "Jenis Barang", "Harga"))
        print("-"*54)
        for i in range(len(data_barang)):
            print("|{:^4}|{:^15}|{:^15}|{:^15}|".format(i,nama_barang[i],jenis_barang[i],harga[i]))
        print("-"*54)
        barang,jumlah = input("Masukkan barang yg dibeli (Namabarang,jumlah beli): ").split(",")

        barang_beli.append(barang)
        jumlah_beli.append(int(jumlah))

        tambah =  input("Tambah barang? [y/n] : ")
        if (tambah == "N") or (tambah =="n"):
            break
        else:
            continue
    

    print("\n{:^61}".format("Struk Belanja"))
    print("-"*61)
    print("|{:^4}|{:^15}|{:^12}|{:^12}|{:^12}|".format("No","Nama Barang","Harga","Jumlah","Total"))
    print("-"*61)
    for k in range(len(barang_beli)):
        if barang_beli[k] in nama_barang:
            index = nama_barang.index(barang_beli[k])
            print("|{:^4}|{:^15}|{:^12}|{:^12}|{:^12}|".format(k,barang_beli[k],harga[index],jumlah_beli[k],(jumlah_beli[k]*harga[index])))
            total += (jumlah_beli[k]*harga[index])
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
