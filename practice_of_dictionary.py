# making a english to hindi distionary and give the opprotunity to user find the meaning in distonary
mydict = {
    "fast": "bhot tez",
    "slow": "dheere",
    "fan":"pankha"
    }
#print("Available option are ",mydict.keys()) #if you want to show the available option of dictonary 

a=input("enter the word what you find in dictionary \n")
# print( " the meaning of",a," is ",mydict[a])
print( " the meaning of",a," is ",mydict.get(a)) #if you avoid the error or not available option in dictonary


# making a dictionary and enter person to enter our favorite language
favlang={}
a=input("Enter raman your favorite language : ")
b=input("Enter hardik your favorite language : ")
c=input("Enter vipin your favorite language : ")
d=input("Enter kashish your favorite language : ")

favlang["raman"]=a
# favlang["vipin"]=a in case two element is same in dictionary then letest value is illegal
favlang["hardik"]=b
favlang["vipin"]=c
favlang["kashish"]=d
print(favlang)