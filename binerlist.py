#Pertanyaan : Tulislah sebuah program dengan input bilanagan biner 4 digit yang dipisahkan koma lalu outputnya
# mencetak bilangan yang habis dibagi 5 , contoh : inputnya 0100,0011,1010,1001  outputnya : 1010

#cara 1 :
x = input("masukan bilangan biner : ")
z = x.split(",")
string = ""
for i in z :
    if int(i,2)%5 == 0 :
        if len(string) == 0 :
            string = i
        else :
            string = string +","+i

print(string)

#cara 2 : 
value = []
items=[i for i in x.split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print(','.join(value))

#fungs int() : untuk mengebalikan sebuah data ke tipe data integer atau bilangan bulat, int(x = , base =)
# dimana base adalah dasar bilanganya jika tidak diisi adalah bilangan dengan dasar 10 jika 2 adalah bilangan biner
