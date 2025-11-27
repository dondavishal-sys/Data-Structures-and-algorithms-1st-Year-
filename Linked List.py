
class Node:
    def __init__(self,val):
        self.data = val
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None 
    
    def insertAtEnd(self,val):
        if self.head == None:
            self.head = Node(val)
            return   
        curr = self.head 
        while curr.next!=None:
            curr = curr.next 
        
        newNode = Node(val)
        curr.next = newNode

    def display(self):
        curr = self.head
        while curr!=None:
            print(curr.data,end="->")
            curr = curr.next 




ll = Linkedlist()
ll.insertAtEnd(10)
ll.insertAtEnd(20)
ll.insertAtEnd(30)
ll.insertAtEnd(40)


ll.display()