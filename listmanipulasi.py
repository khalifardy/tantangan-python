#Pertanyaan : buatlah sebuah program dengan input sebuah string dengan spasi menghasilkan output yang berurutan
#dan tak ada kata yang sama, contoh siapa yang tahu tentang siapa aku akan menghasilkan output : aku siapa tahu tentang yang

#cara 1 :

x = input("masukan kalimat: ")
z = x.split()
string = ""

hasil = list(dict.fromkeys(z))
cetak = sorted(hasil)

for i in cetak :
    if len(string) == 0 :
        string = i
    
    else :
        string = string +" "+i

print(string)
    
#cara 2 :
words = [word for word in x.split(" ")]
print(" ".join(sorted(list(set(words)))))


# fungsi list() : membuat sebuah object menjadi list 
# fungsi set () : sebuat tipe data yang tidak mempunyai anggota yang sama
# fungsi dict.fromkeys() : membuat sebuah dictionary tidak mempunyai nilai data yang sama

