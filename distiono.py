# a distionary made by {} that symbol
mydis = {
    "fast": "bhot tez",
    # to make my option in distionary we ( , )
    "slow": "dheere",
    # we also use int in    `` distionary
    "marks": [1, 5, 9],
    1: 45
}

print(mydis['fast'])

print(mydis.keys())  # we print the all key of dictionary
print(list(mydis.keys()))  # we print the all key of dictionary in list form

print(mydis.values())  # we print the all values of dictionary
print(list(mydis.values()))  # we print the all values of dictionary in list form

print(mydis)  # we print direct distionary like this

# make a another distionary for updating previous distionary
gyan={
    "love":" chutiya banna",
    "paise" : "achi ldki"
}

mydis.update(gyan)  # update the distionary by adding anothor distionary like it
print(mydis)

# most improtant 
# we printing the single value by 2 types
print(mydis.get("love"))  
print(mydis.get("love1")) #we use get funtion to print the single value if that not present in distionary then they return or print none


print(mydis["love"])
# print(mydis["love1"])
#we use [] funtion to print the single value but if that not present in distionary then they gives error
