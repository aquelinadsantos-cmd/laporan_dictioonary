# 1. Meminta input nama file
nama_file = input("Masukkan nama file :")

try:
    # 2. Membuka file
    handle = open(nama_file)
except:
    print("File tidak ditemukan:", nama_file)
    exit()

# 3. Membuat dictionary kosong untuk histogram
counts = dict()

for baris in handle:
    # 4. Hanya proses baris yang diawali 'From '
    if not baris.startswith('From '):
        continue
    
    # 5. Pecah baris menjadi kata-kata
    kata = baris.split()
    
    # 6. Alamat email lengkap ada di indeks ke-1
    email = kata[1]
    
    # 7. Update histogram menggunakan dictionary
    # Jika email sudah ada, tambah 1. Jika belum ada, mulai dari 0 + 1.
    counts[email] = counts.get(email, 0) + 1

# 8. Cetak hasil akhirnya
print(counts)