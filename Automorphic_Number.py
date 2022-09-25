n=int(input())
a=0
sq=n**2
while n:
    if n%10!=sq%10:
        print("Not an Automorphic Number")
        a=1
        break
    n=n//10
    sq=sq//10
    
if a==0:
    print("Automorphic Number")