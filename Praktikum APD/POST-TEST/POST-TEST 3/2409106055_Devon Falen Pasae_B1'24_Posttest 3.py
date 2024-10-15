import os

if os.name == 'nt':
    os.system('cls')

    
print(f"""
======================================================================
         Menu Program Menghitung Luas/Keliling Bangun Datar
======================================================================
1. Luas Persegi
2. Keliling Persegi
3. Luas Segitiga
4. Keliling Segitiga
5. Luas Jajargenjang
6. Keliling Jajargenjang
7. Keluar Program...
=====================================================================
                        """)

pilihan = input("Silahkan pilih ruang datar yang tersedia : ")

if pilihan == '1':
    print("Menghitung luas persegi")
    sisi = float(input("Masukkan panjang sisi:"))
    luas_persegi = (2 * sisi)
    print("Luas Persegi:", luas_persegi)

elif pilihan == '2':
    print("Menghitung keliling persegi")
    sisi =float(input("Masukkan panjang sisi:"))
    keliling_persegi = (4 * sisi)
    print("Keliling Persegi:", keliling_persegi)

elif pilihan == '3':
    print("Menghitung luas segitiga")
    alas = float(input("Masukkan panjang alas segitiga:"))
    tinggi = float(input("Masukkan tinggi segitiga:"))
    luas_segitiga = (0.5 * alas * tinggi)
    print("Luas Segitiga:", luas_segitiga)

elif pilihan == '4':
    print("Menghitung keliling segitiga")
    sisi_a = float(input("Masukkan panjang sisi A"))
    sisi_b = float(input("Masukkan panjang sisi B"))
    sisi_c = float(input("Masukkan panjang sisi C"))
    keliling_segitiga = (sisi_a + sisi_b + sisi_c)
    print("Keliling Segitiga:", keliling_segitiga)

elif pilihan == '5':
    print("Menghitung luas jajargenjang")
    alas = float(input("Masukkan panjang alas"))
    tinggi = float(input("Masukkan tinggi"))
    luas_jajargenjang = (alas * tinggi)
    print("Luas jajargenjang:",luas_jajargenjang)

elif pilihan == '6':
    print("Menghitung keliling jajargenjang")
    sisi_a = float(input("Masukkan panjang sisi A"))
    sisi_b = float(input("Masukkan panjang sisi B"))
    sisi_c = float(input("Masukkan panjang sisi C"))
    sisi_d = float(input("Masukkan panjang sisi D"))
    keliling_jajargenjang = (sisi_a + sisi_b + sisi_c + sisi_d)
    print("Keliling jajargenjang:",keliling_jajargenjang)

elif pilihan =='7':
    print(f"""
    Anda telah keluar dari program!
     Terimakasih telah mencoba!
    """)
    
          





