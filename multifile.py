for i in range(1,6):
   with  open(f"table of {i}","w") as f:
       for j in range (1,11):
           f.write(f"{i} X {j} ={i*j}")


