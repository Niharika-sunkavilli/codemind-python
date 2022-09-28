def palindrome(n):
    a=n
    rev=0
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if(a==rev):
        return True
    else:
        return False

n=int(input())
i=n+1
while True:
    if(palindrome(i)):
        a=i
        break
    i+=1

i=n-1
while True:
    if(palindrome(i)):
        b=i
        break
    i=i-1
    
if(n-b == a-n):
    print(b,a)
elif(n-b>a-n):
    print(a)
else:
    print(b)