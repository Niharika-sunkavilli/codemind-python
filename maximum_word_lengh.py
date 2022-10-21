n=input()
l=list(n.split())
max=len(l[0])
for i in l:
    y=str(i)
    x=len(y)
    if(x>max):
        max=x
print(max)