users = {
    'admin': {'password': 'admin123', 'role': 'admin'},
    'user': {'password': 'user123', 'role': 'user'}
}
Donasi = []

def register_user():
    global users
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")
    role = input("Masukkan role (admin/user): ")

    if role in ['admin', 'user']:
        if username in users:
            print("Username sudah ada, silakan pilih username lain.")
        else:
            users[username] = {'password': password, 'role': role}
            print(f"Registrasi berhasil untuk {username}.")
    else:
        print("Role tidak valid, registrasi gagal.")

def login_user():
    global users
    login_success = False
    while not login_success:
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username]['password'] == password:
            login_success = True
            return users[username]['role']
        else:
            print("Login gagal, coba lagi.")

def admin_menu():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Tambah Donasi\n2. Lihat Donasi\n3. Hapus Donasi\n4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            Tambah_Donasi()
        elif pilihan == '2':
            Lihat_Donasi()
        elif pilihan == '3':
            Hapus_Donasi()
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak ada, silahkan input ulang.")

def user_menu():
    while True:
        print("\n=== MENU USER ===")
        print("1. Lihat Donasi\n2. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            Lihat_Donasi()
        elif pilihan == '2':
            print("Terima kasih karena sudah mau sebagai user.")
            break
        else:
            print("Pilihan tidak valid, silahkan input ulang.")

def Tambah_Donasi():
    nama_donatur = input("Nama Donatur: ")
    jumlah_donasi = input("Jumlah Donasi: ")
    if jumlah_donasi.isdigit():
        Donasi.append({'nama': nama_donatur, 'jumlah': jumlah_donasi})
        print("Donasi berhasil ditambahkan.")
    else:
        print("Jumlah donasi harus berupa angka.")

def Lihat_Donasi():
    if Donasi:
        print("\nDaftar Donasi:")
        for index, donasi in enumerate(Donasi):
            print(f"{index + 1}. {donasi['nama']} - {donasi['jumlah']}")
    else:
        print("Belum ada donasi.")

def Hapus_Donasi():
    if Donasi:
        Lihat_Donasi()
        hapus = input("Nomor donasi yang ingin dihapus: ")
        if hapus.isdigit():
            hapus = int(hapus) - 1
            if 0 <= hapus < len(Donasi):
                del Donasi[hapus]
                print("Donasi berhasil dihapus.")
            else:
                print("Nomor donasi tidak ada, silahkan input ulang.")
        else:
            print("Input tidak valid, harus berupa angka.")
    else:
        print("Belum ada donasi.")

def main():
    print("=== REGISTRASI ===")
    register_user()
    
    print("\n=== LOGIN ===")
    role = login_user()

    if role == 'admin':
        admin_menu()
    else:
        user_menu()

if __name__ == "__main__":
    main()
