#pertanyaan: tulislah sebuah program yang menghasilkan sebuah dictionary dimana value nya adalah hasil kuadrat key nya

x = int(input("masukan bilangan : "))
bilangan = range(1, x+1)
kuadrat = {}

for i in bilangan :
    kuadrat[i]=i*i

print(kuadrat)

#tanda {} adalah dictionary / kamus