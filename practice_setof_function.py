# # find the greater number of four by function

# def max_num(m1, m2, m3, m4):
#     list_of_number = [m1, m2, m3, m4]
#     list_of_number.sort()
#     print(list_of_number[-1])

# m1 = int(input("Enter the number 1 : "))
# m2 = int(input("Enter the number 2 : "))
# m3 = int(input("Enter the number 3 : "))
# m4 = int(input("Enter the number 4 : "))
# max_num(m1, m2, m3, m4)

# # print many print without added new line

# print("hello, ", end="")
# print("how ", end="")
# print("are ", end="")
# print("you ", end="")


# write a program to sum of natural number under the given number
# def natural_num(a):
a = int(input("Enter the number for sum of all  natural number : "))
for i in range(1, (a + 1)):
        for j in range(2, i+1):
            if (i%j == 0):
                break
            else:
                print(i," is prime")


