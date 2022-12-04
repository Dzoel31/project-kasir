import os 
import pandas as pd


def save_data(sort_data_menu):
    saved_data = pd.DataFrame(sort_data_menu, columns=["Nama Menu", "Jenis Menu", "Harga"])
    saved_data.to_csv("data/data_menu.csv", index=False)

def current_data(new_data):
    current_data = pd.read_csv("data/data_menu.csv")
    data_menu = current_data.values.tolist()

    data_menu.append(new_data)

    for i in range(len(data_menu)):
        for j in range(len(data_menu)-i-1):
            if data_menu[j][1] > data_menu[j+1][1]:
                temp = data_menu[j]
                data_menu[j] = data_menu[j+1]
                data_menu[j+1] = temp

    sort_data_menu = data_menu
    save_data(sort_data_menu) 

def add_data():
    nama_menu = input("Masukkan nama menu : ")
    jns_menu = input("Masukkan jenis [Makanan/Minuman] : ")
    harga = int(input("Masukkan harga menu : "))
    new_data = [nama_menu, jns_menu, harga] 
    current_data(new_data)

def show_data():
    current_data = pd.read_csv("data/data_menu.csv")
    data_menu = current_data.values.tolist()
    if data_menu == []: 
        print("Tidak ada data")
        return "Tidak ada data" 
    else: 
        nama_menu,jenis_menu,harga = map(list,zip(*data_menu)) 
        
        print("-"*54)
        print("|{:^4}|{:^15}|{:^15}|{:^15}|".format(
            "No", "Nama Menu", "Jenis menu", "Harga"))
        print("-"*54)
        for i in range(len(data_menu)):
            print("|{:^4}|{:<15}|{:^15}|{:>15}|".format(i,nama_menu[i],jenis_menu[i],harga[i]))
        print("-"*54)

def update_harga():
    check_data = show_data()
    if check_data == "Tidak ada data": 
        print("Buat data terlebih dahulu!")
    else:
        current_data = pd.read_csv("data/data_menu.csv")
        data_menu = current_data.values.tolist()
        try: 
            pilih = int(input("Pilih data yang mau di perbaharui : "))
            upd_harga = int(input("Masukkan harga baru : "))

            print("Nama menu  : ",data_menu[pilih][0])
            print("Harga lama : ",data_menu[pilih][2])
            print("Harga Baru : ",upd_harga)
            check = input("Apakah anda yakin ingin mengubah harga? [Y/N] : ").upper()
            if check == "Y" : 
                data_menu[pilih][2] = upd_harga 
                print("Harga berhasil diubah")
                save_data(data_menu)
            else :
                print("Perubahan harga dibatalkan")

        except ValueError: 
            print("Input harus Integer!!!")
            update_harga()

def delete_data():
    check_data = show_data()
    if  check_data == "Tidak ada data":
        print("Buat data terlebih dahulu!")
    else :
        current_data = pd.read_csv("data/data_menu.csv")
        data_menu = current_data.values.tolist()
        try:
            pilih = int(input("Pilih data yang mau dihapus : "))
            check = input(f"Anda akan menghapus menu {data_menu[pilih][0]} [Y/N] : ").upper() 
            if check == "Y": 
                data_menu.pop(pilih)
                print("Data berhasil dihapus!!")
                save_data(data_menu) 
            else: 
                print("Proses dibatalkan")
        except ValueError:
            print("Input urutannya!")
            delete_data()

def menu_edit():
    status = "Y"
    while status != "N": 
        os.system('cls')
        print("[1] Buat Data/Tambah Data")
        print("[2] Lihat Data")
        print("[3] Update Harga")
        print("[4] Hapus Data")
        print("[5] Menu Sebelumnya")
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
            break 
        else:
            print("Salah input!")
        
        status = input("Next process?[Y/N] => ").upper()