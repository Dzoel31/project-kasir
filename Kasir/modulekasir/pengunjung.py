import os
import pandas as pd
from collections import namedtuple
from modulekasir.inputdata import read_data_menu, getpaths


def read_data_pengunjung():
    path = getpaths()
    read_data = pd.read_csv(f"{path}\\data\\daftar_pengunjung.csv")
    list_data = read_data.values.tolist()
    no_order = read_data["No Order"].drop_duplicates()
    try:
        no_order_duplicate, nama_menu, harga, jumlah, total, tanggal = map(list, zip(*list_data))

    except ValueError:
        no_order_duplicate, nama_menu, harga, jumlah, total, tanggal = ([] for _ in range(6))

    DataPengunjung = namedtuple("ListDataPengunjung", [
                                "list_data",
                                "no_order",
                                "nama_menu",
                                "harga",
                                "jumlah",
                                "total",
                                "tanggal",
                                "no_order_duplicate"])

    return DataPengunjung(list_data,
    no_order,
    nama_menu,
    harga,
    jumlah,
    total,
    tanggal,
    no_order_duplicate)


def lihat_data():
    try:
        os.system('cls')
        data_pengunjung = read_data_pengunjung()
        data_menu = read_data_menu()
        no_order = data_pengunjung.no_order
        menu_jumlah = dict.fromkeys(data_menu.nama_menu, 0)

        for k in range(len(data_pengunjung.nama_menu)):
            jumlah_total = menu_jumlah[data_pengunjung.nama_menu[k]] + data_pengunjung.jumlah[k]
            menu_jumlah[data_pengunjung.nama_menu[k]] = jumlah_total

        print("-"*66)
        print("|{:^64}|".format("Laporan Penjualan"))
        print("-"*66)
        print("|{:^21}|{:^21}|{:^20}|".format("Tanggal Order", "No. Order", "Pemasukan"))
        print("-"*66)
        for l in no_order:
            jumlah = data_pengunjung.no_order_duplicate.count(l)
            indeks = data_pengunjung.no_order_duplicate.index(l)
            nomor = "{:03d}".format(l)
            pemasukan = 0
            for m in range(jumlah):
                pemasukan += data_pengunjung.total[indeks + m]
            print("|{:^21}|{:^21}|{:>20}|".format(data_pengunjung.tanggal[indeks], nomor, pemasukan))
        print("-"*66)
        print("|{:^21}|{:^21}|{:>20}|".format("Banyak Pembeli",len(no_order), sum(data_pengunjung.total)))
        print("-"*66)
        print("|{:^4}|{:^15}|{:^12}|{:^17}|{:^12}|".format("No", "Nama menu", "Harga", "Jumlah Terjual", "Total Harga"))
        print("-"*66)
        for n in range(len(data_menu.nama_menu)):
            Total_harga = data_menu.harga[n] * menu_jumlah[data_menu.nama_menu[n]]
            print("|{:^4}|{:<15}|{:^12}|{:^17}|{:>12}|".format(n+1, data_menu.nama_menu[n], data_menu.harga[n], menu_jumlah[data_menu.nama_menu[n]], Total_harga))
        print("-"*66)
        print("|{:^51}|{:>12}|".format("Total Penjualan", sum(data_pengunjung.total)))
        print("-"*66)
        input("Enter untuk kembali")

    except ValueError:
        input("Belum ada data transaksi! \n Tekan enter untuk lanjut!")

    except FileNotFoundError:
        input("File tidak ditemukan! Periksa kembali alamat atau nama file! \n Tekan enter untuk lanjut!")
