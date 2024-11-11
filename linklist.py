class node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

node1=node(1)
node2=node(4)
node3=node(71)
node4=node(17)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=None

c=node1
while c is not None:
    print(c.data)
    c=c.next
    