#Pertanyaan : buatlah program untuk menghitung a + aa + aaa + aaaa 
x = input('masukan angka :')
n1 = int( "%s" % x )
n2 = int( "%s%s" % (x,x) )
n3 = int( "%s%s%s" % (x,x,x) )
n4 = int( "%s%s%s%s" % (x,x,x,x) )
print(n1+n2+n3+n4)

# %s untuk formating string 