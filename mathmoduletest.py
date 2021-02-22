#Pertanyaan : buatlah sebuah program dimana inpunya bilangan dengan koma dan outpunya hasil akar dari dan koma juga
#cara 1
import math

string = input("masukan angka : ")
x = string.split(",")
cetak = ""
C = 50
H = 30
for i in x :
    D = int(i)
    W = (2*C*D)/H
    Q = int(math.sqrt(W))
    S = str(Q)
    cetak = cetak +","+ S

print(cetak.lstrip(","))
#import module math dibutuhkan untuk banyak operasi matemaatika
#fungsi lstrip() berguna untuk menghilangkan spasi di awal string jika tidak kita pilih

#cara kedua 
li = []
for i in x :
    D = int(i)
    W = (2*C*D)/H
    Q = int(math.sqrt(W))
    S = str(Q)
    li.append(S)

cetak1 = ",".join(li)
print(cetak1)

#fungsi append untuk menambahkan list


