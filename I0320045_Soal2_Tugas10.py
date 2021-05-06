#soal nomor 2
#membuat program biodata diri (menggunakan mode"w") = output berupa file txt

import os

print("")
print("Isi semua data pada formulir biodata diri ini!")
print("")
input("Klik ENTER untuk memulai")
print("")
x = "Biodata Diri.txt"
print(x.center(50))
print("="*50)
print("")
nama = input("Nama Lengkap: ")
umur = int(input("Umur : "))
alamat = input("Alamat Tinggal : ")
hobi = input("Hobi : ")

teks = f"Nama : {nama}\nUmur : {umur}\nAlamat : {alamat}\nHobi : {hobi}"

file = open("dir/biodata_diri.txt","w")
file.write(teks)
file.close()

print("")
print("="*50)
x = "Selesai"
print(x.center(50))
print("")

input("Klik ENTER jika sudah selesai")
print("")