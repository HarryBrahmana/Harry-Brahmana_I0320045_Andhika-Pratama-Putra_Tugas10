#soal nomor 3
#membuat mode "a"/append untuk menambahkan 1 biodata teman anda
import os

print("")
print("Isi semua data pada formulir biodata diri ini!")
print("")
input("Klik ENTER untuk memulai")
print("")
x = "Append ke biodata_diri.txt"
print(x.center(50))
print("="*50)
print("")
nama = input("Nama Lengkap: ")
umur = int(input("Umur : "))
alamat = input("Alamat Tinggal : ")
hobi = input("Hobi : ")

teks = f"\n\nNama : {nama}\nUmur : {umur}\nAlamat : {alamat}\nHobi : {hobi}"

file = open("dir/biodata_diri.txt","a")
file.write(teks)
file.close()

print("")
print("="*50)
x = "Selesai"
print(x.center(50))
print("")

input("Klik ENTER jika sudah selesai")
print("")