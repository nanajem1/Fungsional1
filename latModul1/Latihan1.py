#latihan1
# Fungsi untuk penjumlahan
from logging import _nameToLevel


def add(a, b):
    return a + b

# Fungsi untuk pengurangan
def minus(a, b):
    return a - b

# Fungsi untuk perkalian
def mult(a, b):
    return a * b

# Fungsi untuk pembagian
def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Pembagian oleh nol tidak dapat dilakukan"


# Fungsi tree yang menggabungkan fungsi-fungsi aritmatik
def tree(expression_tree):
    if isinstance(expression_tree, tuple):
        left, operation, right = expression_tree
        if operation == '+':
            return add(tree(left), tree(right))
        elif operation == '-':
            return minus(tree(left), tree(right))
        elif operation == '*':
            return mult(tree(left), tree(right))
        elif operation == '/':
            return div(tree(left), tree(right))
    else:
        return expression_tree


# Contoh penggunaan fungsi tree dengan pohon ekspresi
expression_tree = ((2, '+', 3), '*', (5, '-', 1))
result = tree(expression_tree)
print("Hasil evaluasi pohon ekspresi:", result)


#latihan2
random_list = [105, 3.1, "hello", 737, "python", 2.7, "world", 412, 5.5, "AI"]

# Inisialisasi variabel untuk menyimpan nilai int, float, dan string
int_values = {}
float_values = ()
string_values = []

# Iterasi melalui random_list untuk memisahkan nilai
for item in random_list:
    if isinstance(item, int):
        # Memisahkan angka satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = (item // 100) % 10

        # Menyimpan dalam dictionary
        int_values[item] = (ratusan, puluhan, satuan)
    elif isinstance(item, float):
        # Menambahkan float ke dalam tuple
        float_values += (item,)
    elif isinstance(item, str):
        # Menambahkan string ke dalam list
        string_values.append(item)

# Menampilkan hasil pemisahan
print("\nNilai Integer (dalam bentuk dictionary):")
print(int_values)
print("\nNilai Float (dalam bentuk tuple):")
print(float_values)
print("\nNilai String (dalam bentuk list):")
print(string_values)


#latihan3
# Sistem Penilaian Akhir Mahasiswa
# Fungsi untuk menghitung nilai akhir seorang mahasiswa
def hitung_nilai_akhir(uts, uas):
    return (uts + uas) / 2


# Fungsi untuk menghitung nilai akhir semua mahasiswa
def hitung_nilai_akhir_semua(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(nilai['uts'], nilai['uas'])
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir


# Fungsi untuk menampilkan nilai akhir semua mahasiswa
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("\nHasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))


def main():
    data_mahasiswa = {
        'Haechan': {'uts': 80, 'uas': 95},
        'Jaemin': {'uts': 75, 'uas': 100},
        'Jisung': {'uts': 88, 'uas': 88},
        'Renjun': {'uts': 100, 'uas': 95},

    }

    data_nilai_akhir = hitung_nilai_akhir_semua(data_mahasiswa)
    tampilkan_nilai_akhir(data_nilai_akhir)


if _nameToLevel == "_main_":
    main()