a=0
b=1

num=int(input("enter the term of fibonacci "))
print("fibonacci series\n",a,b ,end=" ")
for i in range (2,num):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
