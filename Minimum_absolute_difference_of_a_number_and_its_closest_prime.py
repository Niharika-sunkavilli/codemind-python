def isprime(n):
    count=0
    for i in range(2,n//2+1):
        if(n%i==0):
            count+=1
    if(count==0):
        return True
    else:
        return False

a=int(input())
for i in range(a,0,-1):
    if(isprime(i)):
        before=i
        break
i=a
while(a>0):
    if(isprime(i)):
        after=i
        break
    i+=1
if(a-before>=after-a):
    print(after-a)
else:
    print(a-before)
