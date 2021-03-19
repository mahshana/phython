n=int(input("enter the limit"))
a=[]
for i in range(n) :
    x=int(input("enter the values"))
    if x>100 :
        a.append('over')
    else :
        a.append(x)
print(a)