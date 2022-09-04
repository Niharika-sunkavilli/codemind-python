def isreverse(n):
    a=n
    sum=0
    while(n>0):
        rem=n%10
        sum=sum*10+rem
        n=n//10
    if(a==sum):
        return True
    else:
        return False
        
    
    
m=int(input())
n=int(input())
for i in range(m,n):
    if isreverse(i):
        print(i,end=" ")