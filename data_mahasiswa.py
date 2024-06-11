# Function to input data
def input_data():
    mahasiswa = []
    n = int(input("masukan jumlah mahasiswa: "))

    for i in range(n):
        print(f"masukan data mahasiswa ke-{i+1}:")
        nama = input("nama: ")
        nim = input("nim: ")
        nilai = float(input("nilai: "))
        mahasiswa_list = {
            "nama": nama,
            "nim": nim,
            "nilai": nilai
        }
        mahasiswa.append(mahasiswa_list)

    return mahasiswa

# Function to display data
def tampilkan(mahasiswa):
    for i, mahasiswa_list in enumerate(mahasiswa):
        print("============================================")
        print(f"mahasiswa ke-{i+1}:")
        print(f"nama: {mahasiswa_list['nama']}")
        print(f"nim: {mahasiswa_list['nim']}")
        print(f"nilai: {mahasiswa_list['nilai']}")

# Function to find the highest and lowest values and calculate the average value
def statistik(mahasiswa):
    if not mahasiswa:
        print("Tidak ada data mahasiswa.")
        return

    nilai_tertinggi = max(mahasiswa, key=lambda x: x['nilai'])
    nilai_terendah = min(mahasiswa, key=lambda x: x['nilai'])
    rata_rata = sum(mahasiswa_list['nilai'] for mahasiswa_list in mahasiswa) / len(mahasiswa)
    print("============================================")
    print(f"Nilai tertinggi:")
    print(f"Nama: {nilai_tertinggi['nama']}, NIM: {nilai_tertinggi['nim']}, Nilai: {nilai_tertinggi['nilai']}")
    print(f"Nilai terendah:")
    print(f"Nama: {nilai_terendah['nama']}, NIM: {nilai_terendah['nim']}, Nilai: {nilai_terendah['nilai']}")
    print(f"Nilai rata-rata: {rata_rata:.2f}")

# Example usage
mahasiswa = input_data()
tampilkan(mahasiswa)
statistik(mahasiswa)
