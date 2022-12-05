def prime(n):
    c=0
    if(n==1):
        return False
    for i in range(2,n//2+1):
        if(n%i==0):
            c+=1
    if(c==0):
        return True
    else:
        return False

n=int(input())
for i in range(2,n//2+1):
    if(n%i==0):
        print(i,end=" ")
        n=n//i
        print(n)
        break
else:
    print(-1)