class info:
    def __init__(self,n,id):
        self.name=n
        self.id=id 
        
    def show(self):
        print(f"name is {self.name} and id is {self.id}")
    @classmethod
    def string(cls,s):
        return cls(s.split("-")[0],s.split("-")[1])
        

s="priyam-1"   
a=info.string(s)
a.show()