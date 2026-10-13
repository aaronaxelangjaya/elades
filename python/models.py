
class Menu:
    def __init__(self, nama_menu, harga, kategori, status="Tersedia"):
        self.nama_menu = nama_menu
        self.harga = harga
        self.kategori = kategori
        self.status = status

    def to_list(self):
        return [
            self.nama_menu,
            self.harga,
            self.kategori,
            self.status
        ]

    def __str__(self):
        return f"{self.nama_menu} - Rp{self.harga} ({self.kategori}) - {self.status}"
