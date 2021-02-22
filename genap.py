#Pertanyaan : Tulis sebuah program, yang akan menemukan semua bilangan antara 1000 dan 3000 (keduanya disertakan) sedemikian rupa sehingga setiap digit bilangan tersebut merupakan bilangan genap.
#Nomor yang diperoleh harus dicetak dalam urutan yang dipisahkan koma dalam satu baris. 

# cara 1 :
x = input("masukan range bilangan : ")
y = x.split(",")
d = ""
e = 0
for i in y :
    if type(d) == str:
        d = int(i)
    
    else :
        e = int(i)

def carigenap(a,b):
    string =""
    for i in range(a,b+1):
        g = str(i)
        if (int(g[0])%2==0 and int(g[1])%2==0 and int(g[2])%2==0 and int(g[3])%2==0) :
            if len(string)== 0 :
                string = g

            else :
                string = string + "," + g
    return string

print(carigenap(d,e))


#cara 2 :

values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))


