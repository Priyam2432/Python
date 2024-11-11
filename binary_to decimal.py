k=input("enter : ")
f=0
decimal1=0
for j in k[::-1]:
    decimal1+=int(j)*(2**f)
    f+=1
print(decimal1)
