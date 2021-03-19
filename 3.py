l1=[1,-5,-7,3,9,-4]
l2=[x for x in l1 if x>0]
print(l2)

#square of n numbers
n=int(input("enter the limit"))
a=[]
for i in range(n):
    x=int(input("enter the numbers"))
    a.append(x)
    l2=[x**2 for x in a]
print(l2)

#list of vowels selected from selected word
word="happy new year"
vowels="aeiou"
v=[x for x in word if x in vowels]
print(v)
l3=[ord(x)for x in word]
print(l3)
