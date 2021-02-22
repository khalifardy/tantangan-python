#Pertanyaan : buatlah sebuah program dengan x,y sebagai input jika kita masukan 3,5 akan menghasilkan output 
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

# cara 1
x = input("masukan bilangan : ")
y = x.split(",")
d = 0
e = 0
for f in y :
    if d == 0:
       d = int(f)
        
    else:
        e = int(f)
    
def carihasil(i,j):
    li1=[]
    a = 0
    while a < i :
        li2 = []
        for b in range(j):
            c = b * a
            li2.append(c)
        li1.append(li2)
        a += 1
    return li1


print(carihasil(d,e))
#fungsi append() untuk menambah list dari belakang    

#cara 2
    
dimensions=[int(v) for v in x.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print(multilist)
