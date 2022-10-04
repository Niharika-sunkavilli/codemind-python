a,b=map(int,input().split())
n=[]
for i in range(a):
    l=list(map(int,input().split()))
    n.append(l)
#print(n)
s1=0
s2=0
for i in range(len(n)):
    for j in range(len(n[i])):
        if i==j:
            s1+=n[i][j]
        if i+j==(b-1) and i!=j:
            s2+=n[i][j]
        a=s1+s2
print(a)

