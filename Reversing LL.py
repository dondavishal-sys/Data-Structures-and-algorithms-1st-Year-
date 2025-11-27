# Create a Linked List
class Node:
    def __init__(self,val):
        self.data = val 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,val):
        temp = Node(val)
        if self.head==None:
            self.head = Node(val)
            return
        
        curr = self.head
        while(curr.next):
            curr = curr.next
        curr.next = temp

    def printLL(self):
        curr = self.head
        while(curr):
            print(curr.data,end="-")
            curr = curr.next
        
        print()
    
    # Reverse LinkedList
    def reverseLL(self):
        if self.head == None:
            return
        if self.head.next == None:
            return self.head

        prev = None
        curr = self.head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)

ll.head = ll.reverseLL()

ll.printLL()
