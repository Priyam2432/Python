class teacher:
    def __init__(self,name ,subject) :
        self.name=name
        self.subject=subject
        
    def show_teacher(self):
        print(f"{self.subject} teach by {self.name}")

class facalty(teacher):
    def show(self):
        print(f"{self.subject} teach by {self.name}")

a=teacher("vkd sir","Os")
a.show_teacher()
b=facalty("ankur sir","CS")
b.show()