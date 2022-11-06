n=input()
v=c=d=w=0
for i in range(len(n)):
    if(n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u' or n[i]=='A' or n[i]=='E' or n[i]=='I' or n[i]=='O' or n[i]=='U'):
        v+=1
    elif(n[i].isdigit()):
        d+=1
    elif(n[i]==' '):
        w+=1
    else:
        c+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",w)