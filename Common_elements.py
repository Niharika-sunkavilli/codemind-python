x,y=map(int,input().split())
a=[]
m=list(map(int,input().split()))
n=list(map(int,input().split()))
#print(m)
#print(n)
for i in range(len(m)):
    for j in range(len(n)):
        if(m[i]==n[j]):
            a.append(m[i])

#print(a)
z=[]
for i in range(len(a)):
    if a[i] not in z:
        z.append(a[i])
        
        
for i in z:
    print(i,end=" ")
#print(z)