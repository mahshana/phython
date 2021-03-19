list1=[1,5,3,4]
list2=[3,5,2,4]
l1=len(list1)
l2=len(list2)
sum1=0
sum2=0
if l1==l2 :
    print("both are in same length")
else :
    print("both are in different length")
for i in list1 :
    sum1=sum1+i
for j in list2 :
    sum2=sum2+j
if sum1==sum2 :
    print("sum are equal")
else :
    print("sum are not equal")
for i in list1:
    for j in list2 :
        if i==j :
            print(j,"is common")



