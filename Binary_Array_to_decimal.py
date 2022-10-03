n=int(input())
l=list(map(int,input().split()))
a=l[::-1]
sum=0
for i in range(len(a)):
    sum+=int(a[i])*2**i
    
print(sum)