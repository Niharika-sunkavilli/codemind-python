a,b=map(int,input().split())
m=list(map(int,input().split()))
n=list(map(int,input().split()))
#print(m)
#print(n)
a=[]
c=0
for i in range(len(m)):
    for j in range(len(n)):
        if(m[i]==n[j]):
            a.append(n[j])
            
z=set(a)
print(len(z))