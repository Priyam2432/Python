# reruired file load in ram if power supply off then lost ram data but some data save in hard disk
# that posible by i/o file program, In i/o file read and write in file data



# some mode of file function
#use open function to read the content

# f=open('sample.text')       # r default mode is read
f = open('sample.text', 'r')  # r apply for read mode
data = f.read()  #that is read mode
# data = f.read(5)  #that read only 5 character only
print(data)
f.close()  # always close file after usages

d=open('sample.text')
data=d.readline()  # Readline read only one line
print(data)
# read second line 
data=d.readline()  # Readline read only  one line
print(data)
d.close()

# that is Write mode of file 
a=open('sample.text','w')
# a.write("put that in sample file")
e=input("Enter the what you write in file : ")
a.write(a)
a.close()

# now the appending part and mode of file functione
# the appending simlar to the write but that not easer previous data of file 
b=open('sample.text','a')  # a for appending
# a.write("put that in sample file")
ap=input("Enter the what you write in file : ")
b.write(ap)
b.close()