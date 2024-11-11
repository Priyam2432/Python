class student:
    def __init__(self,name):
        self.name=name
        
    def show(self):
        print(f"{self.name} is student name")
    
    
class clg:
    def __init__(self,college):
        self.college=college  
    
    def show(self):
        print(f"{self.college} is clg name")
        
class life(clg,student):
    def __init__(self, name,college):
        self.name=name
        self.college=college
        
career=life("Priyam","SRMS")
print(career.name)
print(career.college)
career.show()