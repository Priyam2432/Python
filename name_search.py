# write program for find the name 
c=0
i=input("Enter the first latter : ") 
a1=['ram','sohan','atul','rahul']
for name in a1:
    if name.startswith(i):
        c+=1
        print(name)
print(c)