
while True : 
        ulang = input("Mabar lagi: ")
        
        if ulang == "gk":
            
            break
        
        print("Mabar lagi")


for i in range (1, 10):
    
        if i % 2 == 1:
        
            continue
        
        print(f"Perulangan ke-(i)")


kesempatan = 3 

username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username == "admin" and password == "admin1234":
    print("Berhasil login!")
    
    
else : print("Username atau password salah!")

data = 0 
while data <= 5:
    print(f"Jumlah data: {data}")
    data += 1