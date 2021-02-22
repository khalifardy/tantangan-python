x = input("masukan password anda : ")
y = x.split(",")
values = []
for i in y :
    if (len(i) >= 6 and len(i) <= 12) :
        count_lowwer = 0
        count_upper = 0
        count_char = 0
        count_num = 0
        for z in i :
            
            if z.isupper()== True :
                count_upper += 1
            elif z.islower() == True :
                count_lowwer += 1
            elif z == "#" or z == "$" or z == "@":
                count_char += 1
            elif z.isdigit()== True :
                count_num += 1
            else:
                pass

        if (count_num > 0 and count_lowwer > 0 and count_upper > 0 and count_char > 0  ):
            values.append(i)        
        else:
            pass
        
print(",".join(values))            
