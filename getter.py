class Sum:
    def __init__(self,value1,value2) :
        self.value1=value1
        self.value2=value2
    def show(self):
        return self.value2+self.value1
 
    @property
    def change(self):
        return int(self.value1)**2

a=Sum(10,4)
print(a.show())
print(a.change)

