
import csv
import os
from models import Menu


def simpan_menu():
    print("\n=== TAMBAH DATA MENU KANTIN ===")

    nama_menu = input("Nama Menu : ").strip()
    harga = input("Harga     : ").strip()
    kategori = input("Kategori  : ").strip()

    if not nama_menu or not harga or not kategori:
        print("\n[PERINGATAN] Semua kolom harus diisi!\n")
        return

    try:
        harga = int(harga)
        if harga < 0:
            print("Harga tidak boleh negatif!")
            return
    except ValueError:
        print("Harga harus berupa angka!")
        return

    menu = Menu(nama_menu, harga, kategori)
    file_exists = os.path.exists("menu.csv")


    with open("menu.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize("menu.csv") == 0:
            writer.writerow(["Nama Menu", "Harga", "Kategori", "Status"])

        writer.writerow(menu.to_list())


    print("\n[BERHASIL] Menu berhasil ditambahkan.\n")


def main():
    while True:
        print("=== MENU TAMBAH MENU ===")
        print("1. Tambah Menu")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            simpan_menu()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.\n")


if __name__ == "__main__":
    main()
