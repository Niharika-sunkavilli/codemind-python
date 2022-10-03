t=int(input())
for i in range(t):
    n=int(input())
    a=[]
    while(n>0):
        rem=n%2
        a.append(rem)
        n=n//2
    b=a[::-1]
    for i in b:
        print(i,end="")
    print()