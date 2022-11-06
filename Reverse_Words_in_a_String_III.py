n=input()
a=""
for i in range(len(n)):
    if(n[i]!=' '):
        a=n[i]+a
    else:
        print(a,end=" ")
        a=""
print(a)