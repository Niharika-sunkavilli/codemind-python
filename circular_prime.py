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
rev=0
if(prime(n)):
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if(prime(rev)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
    
    
    