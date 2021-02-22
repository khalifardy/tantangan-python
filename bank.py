#Pertanyaan : buatlah aplikasi perbankan dengan D sebagai deposit dan W sebagai pengeluaran, dengan output total bersih dari rekening 

#Cara 1 :
transaksi=[]
total_bersih = 0

def mula():
    x = input("anda ingin bertransaksi, yes=y , no = n : ")

    if x == "y" or x == "Y":
        main()
    elif x == "n" or x == "N":
        print(transaksi)
        print(total_bersih)
        exit()
    else:
        mula()

def main():
    global total_bersih
    global transaksi
    z = input("masukan transaksi anda : ")
    m = z.split()
    print(m)

    if m[0] == "D" :
        transaksi.append(m)
        total_bersih = total_bersih + int(m[1])
        loop()
    
    elif m[0] == "W" :
        transaksi.append(m)
        total_bersih = total_bersih - int(m[1])
        loop()
    
    else:
        print("input yang anda masukan salah ")
        main()
    

def loop():
    h = input("anda ingin bertransaksi lagi ? : ")

    if h == "y" or h == "Y":
        main()
    elif h == "n" or h == "N":
        print("log transaksi:", transaksi)
        print("total:", total_bersih)
        exit()
    else:
        loop()

mula()


#cara 2:
netAmount = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print(netAmount)

# global berfungsi untuk mendeklarasikan variabel sebagai variabel yang bersifat global
