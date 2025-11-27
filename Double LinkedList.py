
class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
        self.prev = None


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
        newNode.prev = curr


    def displayFromStart(self):
        curr = self.head
        while(curr):
            print(curr.data,end="->")
            curr = curr.next


    def displayFromEnd(self):
        curr = self.head 
        while curr.next!=None:
            curr = curr.next 
        
        while curr!=None:
            print(curr.data,end="->")
            curr = curr.prev


ll = Linkedlist()
ll.insertAtEnd(10)
ll.insertAtEnd(20)
ll.insertAtEnd(30)


ll.displayFromStart()
ll.displayFromEnd()