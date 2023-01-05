

def palindrome(n):
    s=0
    while(n>0):
        rem=n%10
        s=s*10+rem
        n=n//10
    return s

def check(n):
    s=0
    a=n
    while(n>0):
        rem=n%10
        s=s*10+rem
        n=n//10
    if(a==s):
        return True
    else:
        return False
    
n=int(input())
a=palindrome(n)
z=a+n
if(check(z)):
    print(z)
else:
    while True:
        z=z+palindrome(z)
        
        if(check(z)):
            print(z)
            break
        else:
            continue
