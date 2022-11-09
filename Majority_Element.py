n=int(input())
l=list(map(int,input().split()))
max=e=0
for i in range(len(l)):
    c=l.count(l[i])
    if(c>max):
        max=c
        e=l[i]
print(e)