import string

# 1. Meminta input nama file dari user
nama_file = input("Masukkan nama file: ")

try:
    # 2. Mencoba membuka file
    handle = open(nama_file)
except:
    # Jika file tidak ditemukan atau salah nama
    print("File tidak dapat dibuka:", nama_file)
    exit()

counts = dict()

# 3. Membaca file baris demi baris
for baris in handle:
    # Cari baris yang diawali dengan 'From ' (bukan 'From:')
    if not baris.startswith('From '):
        continue
    
    # Pecah baris menjadi daftar kata
    kata = baris.split()
    
    # Email ada di kata kedua (index 1)
    email = kata[1]
    
    # 4. Ambil domain (teks setelah tanda '@')
    # split('@') memecah email menjadi [username, domain]
    bagian = email.split('@')
    domain = bagian[1]
    
    # 5. Hitung jumlah kemunculan domain menggunakan metode .get()
    # Jika domain belum ada di dict, beri nilai awal 0 lalu tambah 1
    counts[domain] = counts.get(domain, 0) + 1

# 6. Tampilkan hasil akhir dictionary
print(counts)