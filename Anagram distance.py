# Write your code here
a_=input("Enetr first String")
b_=input("Enetr Second String")
a=[]
b=[]
for z in a_:
    a.append(z)
for y in b_:
    b.append(y)
alen=len(a)
blen=len(b)
flag=True
temp=a.copy()
# arr=[0]*26
# arr2=[0]*26
if alen!=blen:
    
    if(alen<blen):
        xyz=b.copy()
        b=a.copy()
        a=xyz.copy()
        temp=a.copy()
    
count=0

for x in a:
    if x not in b:
        count+=1
    else:
        b.remove(x)
    temp.remove(x)

count=len(b)+len(temp)+count




print (count)

        
