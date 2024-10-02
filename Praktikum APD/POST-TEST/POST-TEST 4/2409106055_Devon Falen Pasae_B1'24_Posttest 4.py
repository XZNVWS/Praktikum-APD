import os
import time

if os.name == 'nt':
    os.system('cls')

username = "Devon"
password = "055"
total_percobaan = 3


for percobaan in range(total_percobaan):
    print(f"""
===========================
          LOGIN
===========================
          """)
    
    
    input_username = input("Masukkan Username: ")
    input_password = input("Masukkan Password: ")
    sisa_percobaan = total_percobaan - (percobaan + 1)


    if input_username != username:
        print(f"""
    Username salah!
    Sisa Percobaan : {sisa_percobaan}
        """)
        time.sleep(4)
    elif input_password != password:
        print(f"""
    Password salah!
    Sisa Percobaan : {sisa_percobaan}
        """)
        time.sleep(4)
    else:
        print("Login berhasil, menuju program...")
        time.sleep(3)
        break  

    os.system('cls')

else:
    print(f"Program terkunci karena Username/Password salah. Harap hubungi administrator bila ini adalah kesalahan")
    time.sleep(5)
    exit()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
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
    pilihan = input("Silahkan pilih ruang datar yang tersedia: ")

    if pilihan == '1':
        print("Menghitung luas persegi")
        sisi = float(input("Masukkan panjang sisi: "))
        luas_persegi = sisi * sisi
        print("Luas Persegi:", luas_persegi)

    elif pilihan == '2':
        print("Menghitung keliling persegi")
        sisi = float(input("Masukkan panjang sisi: "))
        keliling_persegi = 4 * sisi
        print("Keliling Persegi:", keliling_persegi)

    elif pilihan == '3':
        print("Menghitung luas segitiga")
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas_segitiga = 0.5 * alas * tinggi
        print("Luas Segitiga:", luas_segitiga)

    elif pilihan == '4':
        print("Menghitung keliling segitiga")
        sisi_a = float(input("Masukkan panjang sisi A: "))
        sisi_b = float(input("Masukkan panjang sisi B: "))
        sisi_c = float(input("Masukkan panjang sisi C: "))
        keliling_segitiga = sisi_a + sisi_b + sisi_c
        print("Keliling Segitiga:", keliling_segitiga)

    elif pilihan == '5':
        print("Menghitung luas jajargenjang")
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas_jajargenjang = alas * tinggi
        print("Luas Jajargenjang:", luas_jajargenjang)

    elif pilihan == '6':
        print("Menghitung keliling jajargenjang")
        sisi_a = float(input("Masukkan panjang sisi A: "))
        sisi_b = float(input("Masukkan panjang sisi B: "))
        keliling_jajargenjang = 2 * (sisi_a + sisi_b)
        print("Keliling Jajargenjang:", keliling_jajargenjang)

    elif pilihan == '7':
        print(f"""
    Anda telah keluar dari program!
     Terimakasih telah mencoba!
    """)
        break 

    else:
        print("Pilihan tidak valid, silakan coba lagi.")
        input("Tekan Enter untuk melanjutkan...")

    
          





