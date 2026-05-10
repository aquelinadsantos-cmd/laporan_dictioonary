# 1. Definisikan dua list yang akan digabungkan
Lista = ['red', 'green', 'blue']
Listb = ['#FF0000', '#008000', '#0000FF']

# 2. Gabungkan menggunakan fungsi zip() dan ubah menjadi dictionary dengan dict()
hasil_dictionary = dict(zip(Lista, Listb))

# 3. Tampilkan hasilnya
print(hasil_dictionary)