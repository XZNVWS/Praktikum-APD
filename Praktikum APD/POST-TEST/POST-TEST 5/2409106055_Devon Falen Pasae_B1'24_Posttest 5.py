import os

if os.name == 'nt':
    os.system('cls')

users = [['admin', 'admin123', 'admin'], ['user', 'user123', 'user']]
Donasi = []

print("=== REGISTRASI ===")
username = input("Masukkan username baru: ")
password = input("Masukkan password baru: ")
role = input("Masukkan role (admin/user): ").lower()

if role in ['admin', 'user']:
    users.append([username, password, role])
    print(f"Registrasi berhasil untuk {username}.")
else:
    print("Role tidak valid, registrasi gagal.")

os.system('cls')

print("\n=== LOGIN ===")
login_success = False
while not login_success:
    username = input("Username: ")
    password = input("Password: ")

    for user in users:
        if user[0] == username and user[1] == password:
            login_success = True
            role = user[2]
            break
    if not login_success:
        print("Login gagal, coba lagi.")

if role == 'admin':
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Tambah Donasi\n2. Lihat Donasi\n3. Hapus Donasi\n4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            nama_donatur = input("Nama Donatur: ")
            jumlah_donasi = input("Jumlah Donasi: ")
            Donasi.append([nama_donatur, jumlah_donasi])
            print("Donasi berhasil ditambahkan.")
        elif pilihan == '2':
            if Donasi:
                print("\nDaftar Donasi:")
                for index, donasi in enumerate(Donasi):
                    print(f"{index+1}. {donasi[0]} - {donasi[1]}")
            else:
                print("Belum ada donasi.")
        elif pilihan == '3':
            if Donasi:
                for index, donasi in enumerate(Donasi):
                    print(f"{index+1}. {donasi[0]} - {donasi[1]}")
                hapus = int(input("Nomor donasi yang ingin dihapus: ")) - 1
                if 0 <= hapus < len(Donasi):
                    del Donasi[hapus]
                    print("Donasi berhasil dihapus.")
                else:
                    print("Nomor donasi tidak ada, silahkan input ulang.")
            else:
                print("Belum ada donasi.")
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak ada, silahkan input ulang.")
else:
    while True:
        print("\n=== MENU USER ===")
        print("1. Lihat Donasi\n2. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            if Donasi:
                print("\nDaftar Donasi:")
                for donasi in Donasi:
                    print(f"{donasi[0]} - {donasi[1]}")
            else:
                print("Belum ada donasi.")
        elif pilihan == '2':
            print("Terima kasih atas partisipasinya!")
            break
        else:
            print("Pilihan tidak valid, silahkan input kembali.")
