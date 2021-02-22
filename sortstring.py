#Pertanyaan : Buatlah sebuah program yang bisa menerima koma sebagai separasi dan mencetak string sesuai 
# dengan urutan abjad 

# cara 1 :

x = input("masukan kata : ")
string = x.split(",")
sortir = sorted(string)
cetak = ""

for i in sortir :
    cetak = cetak + "," + i


print(cetak.lstrip(","))

#cara 2 
items=[x for x in input().split(',')]
items.sort()
print(','.join(items))