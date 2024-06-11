# ANSI escape code untuk warna
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

# membuat inventaris barang
# tambahkan item
def tambah_barang(inventaris):
    print(f"{YELLOW}================================={RESET}")
    nama = input("Nama barang: ")
    kode = input("Kode barang: ")
    jumlah = int(input("Jumlah barang: "))
    barang = {
        "nama": nama,
        "kode": kode,
        "jumlah": jumlah
    }
    # untuk menambahkan barang
    inventaris.append(barang)
    print(f"{GREEN}Barang berhasil ditambahkan!{RESET}")

# untuk menampilkan barang
def tampilkan_barang(inventaris):
    if not inventaris:
        print("Tidak ada barang dalam inventaris.")
        return
    print("Daftar Barang:")
    for i, barang in enumerate(inventaris):
        print(f"{YELLOW}================================={RESET}")
        print(f"Barang ke-{i+1}:")
        print(f"Nama: {barang['nama']}")
        print(f"Kode: {barang['kode']}")
        print(f"Jumlah: {barang['jumlah']}")

# cari barang sesuai code
def cari_barang(inventaris, kode):
    for barang in inventaris:
        if barang['kode'] == kode:
            print(f"{YELLOW}================================={RESET}")
            print("Barang ditemukan:")
            print(f"Nama: {barang['nama']}")
            print(f"Kode: {barang['kode']}")
            print(f"Jumlah: {barang['jumlah']}")
            return
    print(f"{RED}Barang dengan kode tersebut tidak ditemukan.{RESET}")

# hapus item
def hapus_barang(inventaris, kode):
    for barang in inventaris:
        if barang['kode'] == kode:
            inventaris.remove(barang)
            print("Barang berhasil dihapus!")
            return
    print("Barang dengan kode tersebut tidak ditemukan.")

def kelola_inventaris():
    inventaris = []
    while True:
        print("=====================================")
        print(f"{YELLOW}toko jaya abadi{RESET}")
        print("=====================================")
        print("\nMenu:")
        print("1. Tambah Barang")
        print("2. Tampilkan Semua Barang")
        print("3. Cari Barang Berdasarkan Kode")
        print("4. Hapus Barang Berdasarkan Kode")
        print("5. Keluar")
        pilihan = input("Pilih angka pada menu: ")

        if pilihan == '1':
            tambah_barang(inventaris)
        elif pilihan == '2':
            tampilkan_barang(inventaris)
        elif pilihan == '3':
            kode = input("Masukkan kode barang yang dicari: ")
            cari_barang(inventaris, kode)
        elif pilihan == '4':
            kode = input("Masukkan kode barang yang akan dihapus: ")
            hapus_barang(inventaris, kode)
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Run the inventory management system
kelola_inventaris()
