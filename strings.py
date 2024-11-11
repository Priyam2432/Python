# we use ''' for multiple line strings
a = '''helllo guys kaise ho 
aap
'''
b = "i wish ache honge"
# adding two string
print(a + b)

# slice in string
value = "hello friend"
print(value[0:7])

# if we not entered any address in starting then it aassum a lowest addess same in last the it assum a hightest address
print(value[0:])

# print given address value of character
print(value[4])

# skiping  charter like this
example = "morningwithgood"
# in given example the complier print string but skip every 2nd charcter
print(example[0::2])