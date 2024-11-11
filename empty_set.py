# important:this syntax create a empty distionary not a empty set 
a={}
print(type(a)) # now they print distionary not a set

# can we created set by using below syntax 
b=set()
print(type(b))
print(b)
b.add(4) #adding the element in the set like it
b.add(98)
b.add((4,6,8))
# b.add([4,6,8]) we not adding a list or distionary in set 
print(b)
b.remove(4) #remove the element in the set like it
print(b)


       
