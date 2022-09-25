def prime(n):
    c=0
    if n==1:
        return False
    for i in range(2,n//2+1):
        if(n%i==0):
            c+=1
    if(c==0):
        return True
    else:
        return False

n=int(input())
c=0
p=0
if(prime(n)):
    while(n>0):
        rem=n%10
        c+=1
        n=n//10
        if(prime(rem)):
            p+=1
    if(p==c):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
            