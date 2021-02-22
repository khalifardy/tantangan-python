#pertanyaan :buatlah sebuah program untuk mengembalikan nilai input sebagai tuple, dengan input sepert 1,2,3,4 dst


x = input("masukan input : ")
li= x.split(",")
hasil = tuple(li)

print(li)
print(hasil)

#fungsi split() adalah untuk mengembalikan string menjadi sebuah list dengan input pembatas jika tidak diisi defaultnya adaklah spasi
