a=[]
c=0
count=0
n=int(input("enter size of list : "))
for i in range(n):
    j=int(input("Enter element : "))
    a.append(j)
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if a[i]==a[j]:
            c+=1
    if c>count:
        max=a[i]
        count=c
print("Output : ",max)      