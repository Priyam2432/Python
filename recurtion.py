# resurtion call by own function

# a=int(input("Enter a number for factorial : "))
# n=a
# j=1
# for i in range(1,(n+1)):
#     j=j*i

# print("Factorial of",a,"is",j)


def factorial(a):
    n = a
    j = 1
    for i in range(1, (n + 1)):
        j = j * i
    print("Factorial of", a, "is", j)

a=int(input("Enter a number for factorial : "))
factorial(a)