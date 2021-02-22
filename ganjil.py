#Pertanyaan :buatlah sebuah program dengan output bilangan ganjil semua

#cara 1 :
x = input("masukan bilangan :")
y = x.split(",")
ganjil = []
kuadrat = []
for i in y :
    if int(i)%2 != 0 :
        ganjil.append(i)
    else:
        pass

for z in ganjil:
    m = int(z)*int(z)
    kuadrat.append(str(m))

hasil = ",".join(ganjil)
hasil2 = ",".join(kuadrat)

print(hasil)
print(hasil2)

#cara 2 :
numbers = [x for x in x.split(",") if int(x)%2!=0]
print(",".join(numbers))