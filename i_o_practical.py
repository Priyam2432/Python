# #find something in text file
# f=open('sample.text')
# t=f.read()
# a=input("enter what you want to search in file : ")
# if a in t:
#     print(f"{a} is present in file")
# else:
#     print(f"{a} is not present in file")
# f.close()



# # # update high score in game file
# def game():
#     return 4506

# score=game()
# f=open("R_P_S_highscore.text")
# hiscore=int(f.read())

# if hiscore<score:
#     f=open('R_P_S_highscore.text','w')
#     f.write(str(score))
# f=open("R_P_S_highscore.text")
# hiscore=(f.read())
# print(f"highscore is {hiscore}")h

with open("hiscore.text") as f:
   a= f.read()

replace=a.replace("hello","####")
with open("hiscore.text","w") as f:
    f.write(replace)


