
class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
        self.prev = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def displayFromStart(self):
        curr = self.head
        while (curr!=None):
            print(curr.data,end="->")
            curr = curr.next

        print()

    def displayFromEnd(self):
        curr = self.head 
        while curr.next!=None:
            curr = curr.next 
        
        while curr!=None:
            print(curr.data,end="->")
            curr = curr.prev
        
        print()

    def insertatBegin(self,val):

        if self.head ==None:
            newhead = Node(val)
            self.head = newhead
            return

        newhead = Node(val)
        newhead.next = self.head 
        self.head.prev = newhead

        self.head = newhead

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

    def insertatMiddle(self,val):
        len = 0
        curr = self.head

        while(curr):
            len+=1
            curr = curr.next

        # print("len:",len,"| mid:",len//2)
        mid = len//2

        # If inserting at the head (mid == 0)
        if mid == 0:
            newNode = Node(val)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            return
        
        curr = self.head
        curr_len = 0
        while curr:
            if curr_len==mid:
                prevNode = curr.prev
                newNode = Node(val)

                prevNode.next = newNode
                newNode.prev = prevNode
                newNode.next = curr
                curr.prev = newNode
                return
            
            curr_len+=1
            curr = curr.next




ll = Linkedlist()
ll.insertAtEnd(10)
ll.insertAtEnd(20)
ll.insertAtEnd(30)
ll.insertAtEnd(40)
# ll.insertAtEnd(50)

# add an element at starting 
ll.insertatBegin(5)


# insert at middle
ll.insertatMiddle(99)


ll.displayFromStart()
ll.displayFromEnd()
