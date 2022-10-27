m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
z=[]
for i in range(len(a)):
    for j in range(len(b)):
        if(a[i]==b[j]):
            z.append(a[i])
x=[]
for i in range(len(z)):
    if z[i] not in x:
        x.append(z[i])
for i in x:
    print(i,end=" ")

