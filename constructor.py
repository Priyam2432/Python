class sum:
    def __init__(self,a,b) -> None:
        
        self.a=int(a)
        self.b=int(b)
    def info (self):
        print(f"{self.a}+{self.b} = {self.a+self.b}")
        
test=sum(10,14)
test.info()
