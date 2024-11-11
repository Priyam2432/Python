 #print the star in a patten

# for i in range(1,4):
#     print("*"*i) 


# print star in a tringle shape 
n=3
for i in range(3):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1),end="") 
    print(" "*(n-i-1),end="")