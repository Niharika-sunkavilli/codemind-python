t=int(input())
for i in range(t):
    n=input()
    s=0
    a=n[::-1]
    l=list(a)
    for i in range(len(a)):
        s=s+int(l[i])*pow(2,i)
    print(s)