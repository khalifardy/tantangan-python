#Pertanyaan : Buatlah sebuah program yang bisa menghitung berapa jumlah angka dan berapa jumlah huruf yang berada dalam satu kalimat
#cara 1 :
x = input("masukan karakter: " )
y = x.split()
digit = 0
letter = 0
for i in y :
    for z in i :
        if z.isdigit() == True :
            digit += 1
        
        elif z.isalpha() == True :
            letter += 1

        else:
            pass                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    

print("letter :", letter)
print("digit: ",digit)



#cara 2 :
d={"DIGITS":0, "LETTERS":0}
for c in x:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1   
    else:
        pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])


#fungsi isdigit() : akan menghasilkan nilai True jika dalam sebuah string berisi angka semua
#fungsi isalpha() : akan menghasilkan nilai True jika dala sebuah string berisi huruf semua