import time
def while_check():
    i=0
    while(i<10):
        print("priyam")
        i+=1
    
def for_check():
    j=0
    for i in range(10):
        print("priyam")
        j+=1

i=time.time()
while_check()
print(time.time()-i)