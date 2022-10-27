t=int(input())
for i in range(t):
    s=input()
    a=s[::-1]
    if(a==s):
        if(len(a)%2==0):
            c="EVEN"
            print("YES",c)
        else:
            print("YES","ODD")
    else:
        print("NO")