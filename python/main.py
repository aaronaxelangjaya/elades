
import subprocess


def buka_tambah_menu():
    subprocess.run(["python", "tambah_menu.py"])


def buka_tampil_menu():
    subprocess.run(["python", "tampil_menu.py"])


def menu_utama():
    while True:
        print("\n" + "=" * 40)
        print(" SISTEM MENU KANTIN ".center(40, "="))
        print("=" * 40)
        print("1. Tambah Menu")
        print("2. Tampilkan Menu")
        print("0. Keluar")
        print("=" * 40)

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            buka_tambah_menu()
        elif pilihan == "2":
            buka_tampil_menu()
        elif pilihan == "0":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    menu_utama()
