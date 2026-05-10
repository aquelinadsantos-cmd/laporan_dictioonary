# 1. Membuat dictionary sesuai contoh soal
data = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# 2. Mencetak header (judul kolom)
# Kita gunakan spasi atau tab agar lurus
print("key   value   item")

# 3. Inisialisasi penghitung untuk kolom 'item'
nomor_item = 1

# 4. Melakukan perulangan untuk mengambil key dan value
for k, v in data.items():
    # Mencetak data dengan format yang rapi
    # k = key, v = value, nomor_item = item
    print(f"{k:<5} {v:<7} {nomor_item}")
    
    # Tambahkan 1 ke nomor_item untuk baris berikutnya
    nomor_item += 1