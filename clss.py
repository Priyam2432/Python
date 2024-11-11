class test:
    def __init__(self,name=None,course=None):
        self.name=name
        self.course=course
    def set(self,name):
        self.name=name
        

n=test()
n.set("Priyam")
print(n.name,n.course)
    