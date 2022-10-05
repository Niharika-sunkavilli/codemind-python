n=int(input())
l=list(map(int,input().split()))
sum=c=0
for i in range(len(l)):
    sum+=l[i]
a=sum//n
for i in range(len(l)):
    if l[i]<=a:
        c+=1
print(c)