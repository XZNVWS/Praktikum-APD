
nama = input("Masukkan nama :") 
umur = int(input("Masukkan umur (tahun) :")) 
tinggi_badan = float(input("Tinggi badan (cm) : "))
berat_badan = float (input("Berat badan (kg) : "))  
status_mahasiswa = (input("Status mahasiswa (aktif/tidak aktif) : ")).lower()

jumlah_variabel = (umur + tinggi_badan + berat_badan)

print(f"""
=============================
        Bio Data Anda
=============================
Nama               : {nama}
Umur               : {umur}
Tinggi badan       : {tinggi_badan}
Berat badan        : {berat_badan}
Status Mahasiswa   : {status_mahasiswa}
Jumlah Variabel    : {jumlah_variabel}     
=============================""")