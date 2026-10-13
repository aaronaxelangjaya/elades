
import csv
import os
from models import Menu


def muat_data():
    daftar_menu = []

    if not os.path.exists("menu.csv"):
        print("File menu.csv tidak ditemukan.")
        return daftar_menu

    with open("menu.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if len(row) < 4:
                continue

            menu = Menu(
                nama_menu=row[0],
                harga=row[1],
                kategori=row[2],
                status=row[3]
            )
            daftar_menu.append(menu)

    return daftar_menu


def tampilkan_menu():
    daftar_menu = muat_data()

    if not daftar_menu:
        print("Belum ada menu kantin.")
        return

    print("\n=== DAFTAR MENU KANTIN ===\n")
    print(f"{'Nama Menu':25}{'Harga (Rp)':15}{'Kategori':20}{'Status'}")
    print("-" * 75)

    for menu in daftar_menu:
        try:
            harga = f"{int(menu.harga):,}".replace(",", ".")
        except (ValueError, TypeError):
            harga = str(menu.harga)

        print(
            f"{menu.nama_menu:25}"
            f"{harga:15}"
            f"{menu.kategori:20}"
            f"{menu.status}"
        )

    print("-" * 75)
    print(f"Total Menu: {len(daftar_menu)}")


def main():
    while True:
        print("\n=== MENU TAMPILKAN MENU ===")
        print("1. Tampilkan Menu")
        print("2. Refresh Data")
        print("0. Keluar")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            tampilkan_menu()
        elif pilihan == "2":
            print("Data dimuat ulang...")
            tampilkan_menu()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()

