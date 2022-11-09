n=int(input())
l=list(map(int,input().split()))
c=max=0
for i in range(len(l)):
    if(l.count(l[i])==1):
        if(l[i]>max):
            max=l[i]
            c+=1
    
if(c==0):
    print(-1)
else:
    print(max)