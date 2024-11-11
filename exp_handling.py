a=input("enter a number for table : ")
try:
    print(f"Table of {int(a)}")
    for i in range(1,11):
        print(f"{a}X{i}={int(a)*i}")
except:
    print("invalid Enter")