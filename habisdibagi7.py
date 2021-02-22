#Pertanyaan : Tulislah program yang akan menemukan semua bilangan yang habis dibagi 7 tetapi bukan kelipatan 5, antara 2000 dan 3200 (keduanya disertakan).
#Nomor yang diperoleh harus dicetak dalam urutan yang dipisahkan koma dalam satu baris. 



list_7 = []
#string =""
angka = range(2000, 3201)

for i in angka:
    if i%7 == 0 and i%5 != 0 :
        list_7.append(str(i))
        #string = string +"," + str(i)

print(",".join(list_7))
#print(string)
#fungsi join berfungsi untu menggabungkan string yang ingin disisipkan antar indeks di dalam sebuah list 
# kemudian mengembalikannya lagi menjadi nilai string
# fungsi Range() mengembalikan nilai dari start (default 0) sampai end (tidak termasuk) range(start, end)
# contoh range(3), akan mengembalikan nilai 0,1,2 
# range (2,5) mengembalikan nilai (2,3,4)
 