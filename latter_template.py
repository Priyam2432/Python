latter='''Dear <|name|>
good news for you 
you are selected for job in tcl
that post you will applied 
reported in TCS office
on <|date|>'''

# we use replace fuction 
name=input("Enter the name ")
date=input("Enter the date ")
latter=latter.replace("<|name|>",name)
latter=latter.replace("<|date|>",date)

# printing latter 
print(latter)

# exit=input("Press any key to Exit ")