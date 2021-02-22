#Pertanyaan: buatlah sebuah program dimana outputnya adalah jumlah huruf besar dan huruf kecil dalam sebuah kalimat 

#cara 1 :

x = input("masukan kalimat : ")

upper = 0
lower = 0 

for i in x :
    if i.isupper()==True:
        upper += 1

    elif i.islower()==True:
        lower += 1

    else: 
        pass

print("upper :",upper)
print("lower :",lower)


#cara2 :
d={"UPPER CASE":0, "LOWER CASE":0}
for c in x:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print("UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])

#fungsi isupper(): mengembalikan nilai True jika sebuah string berisi huruf besar semua
#fungsi islowwer() : mengembalikan niai True jika sebuah string bersisi huruf kecil semua