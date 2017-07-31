def isPal(pal):
    str_pal=str(pal)
    
    checker = False
    for z in range(1,len(str_pal)):
        if str_pal[-z]==str_pal[z-1]:
            checker = True
        else:
            return False
    return True

temp = 0
for x in range(1000,100,-1):
    for y in range(1000,100,-1):
        product=x*y
        if(isPal(product)):
            if(product > temp):
                print(product)
                temp = product
        
