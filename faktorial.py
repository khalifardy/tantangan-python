#pertanyaan : tulislah program yang menghasilkan nilai faktorial dari sebuah bilangan n 

#ada dua cara
#cara pertama :
x = int(input("masukan bilangan : "))
bilangan = range(x,0,-1)
hasil = 0

if x == hasil :
    hasil = 1
else:
    for i in bilangan:
        if hasil == 0 :
            hasil += i
        else:
            hasil = hasil * i

print(hasil)

#cara kedua
def fact(x):
    if x == 0 :
        return 1
    else:
        return x * fact(x-1)

print(fact(x))

