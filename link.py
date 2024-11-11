# singly link list 
class node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class sll:
    def __init__(self,start=None) :
        self.start=start
        
    def is_empty(self,start):
        return self.start==None
    
    def insert_start(self,data):
       n=node(data,self.start)
       self.start=n
    
    def insert_last(self,data):
        n=node(data)
        if not self.is_empty():
            t=self.start
            while t.next is not None:
                t=t.next 
    def search(self,data):
        t=self.start
        while t.next is not None:
            if t.item==data:
                return data
        return None
            
            
    
    
test=sll()