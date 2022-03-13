from os import system
from sains import matematika

"""
    Aplikasi Oleh       : Adhitya Febhiakbar.
    Info Version        : 
        1. Versi 1      : 13 Maret 2022

    Belajar membuat aplikasi sederhana menggunakan Python.
    Hal yang ingin coba diimplementasi :
    1. Package dan Module
    2. Comment
    3. Method input dan print
    4. Format string
    5. If statement
    6. Membuat executable file
    7. Conversion
"""

# Inisiasi Program
# Masukkan Nama Pengguna
nama = input('Masukkan nama anda\t: ')
print(f"\nHalo {nama} Selamat Datang!\n")

while True:
    print("="*10,"Program Scientific","="*10)
    print(f"1. Operasi Tambah")
    print(f"2. Operasi Kurang")
    print(f"3. Operasi Kali")
    print(f"4. Operasi Bagi")

    # Masukkan data pilihan operasi
    choiceOperation = int(input('Pilih Operasi\t: '))
    
    # Masukkan data angka
    angka1 = float(input('Masukkan angka 1\t: '))
    angka2 = float(input('Masukkan angka 2\t: '))

    # Jika pilihan adalah operasi tambah
    if choiceOperation == 1:
        matematika.tambah(angka1, angka2)

    # Jika pilihan adalah operasi kurang
    elif choiceOperation == 2:
        matematika.kurang(angka1, angka2)

    # Jika pilihan adalah operasi kali
    elif choiceOperation == 3:
        matematika.kali(angka1, angka2)
    
    # Jika pilihan adalah operasi bagi
    elif choiceOperation == 4:
        matematika.bagi(angka1, angka2)
    
    # Jika pilihan tidak valid
    # diarahkan kembali ke saat memilih operasi
    else:
        print("Harap Masukkan Pilihan yang tersedia!")
        system('cls')
        continue

    choice = input('Ingin melanjutkan program? (y/n)\t: ')

    # Jika tidak ingin melanjutkan program
    if choice == "n":
        break

    # Jika ingin melanjutkan program
    else:
        system('cls')

print(f"\nTerima kasih telah menggunakan aplikasi ini {nama}!\n")
system("pause")