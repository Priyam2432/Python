                        #      # Map
# def cube(x):
#     return x*x*x
# l=[1,2,3,4,5,6,7]

# # # by return by function

# # newl=map(cube,l)    #it return in map
# # newl=list(map(cube,l))   # here change map to list

# # using lambda 
# newl=map(lambda x:x**3,l)    #it return in map
# newl=list(map(lambda x:x*x*x,l))   # here change map to list 
# # newl=list(map(lambda x:x**3,l))   # here change map to list and here using power function
# print(newl)


#                             # filter

# l=[1,2,3,4,5,6,7,8,10]
# newl=list(filter(lambda x:x>5,l))  #here filter only true value
# print(newl)


                               # reduce

from functools import reduce      #here importing reduce
l=[1,2,3,4,5,6,7,8,10]
sum=reduce(lambda x,y:x+y,l)
print(sum)