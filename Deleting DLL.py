
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

    def deleteHead(self):
        if self.head == None:
            return
        
        if self.head.next == None:
            self.head = None
            return
        
        newHead = self.head.next
        newHead.prev = None
        self.head = newHead

    def deleteTail(self):
        if self.head ==None:
            return
        
        if self.head.next == None:
            self.head = None
            return

        curr = self.head
        while curr.next!=None:
            curr = curr.next 
        
        prevNode = curr.prev 
        prevNode.next = None

    def deleteMiddle(self):
        if self.head ==None:
            return
        
        if self.head.next == None:
            self.head = None
            return        

        len = 0
        curr = self.head

        while curr!=None:
            len+=1
            curr = curr.next
        mid = len//2
        print("len: ",len,"| mid : ",mid )

        curr_len = 0
        curr = self.head
        while curr!=None:
            if curr_len ==mid:
                prevNode = curr.prev
                nextNode = curr.next 
                prevNode.next = nextNode
                nextNode.prev = prevNode
                return
            
            curr_len+=1
            curr = curr.next

ll = Linkedlist()
ll.insertAtEnd(10)
ll.insertAtEnd(20)
ll.insertAtEnd(30)
ll.insertAtEnd(40)
ll.insertAtEnd(50)

# ll.deleteHead()
# ll.deleteTail()
ll.deleteMiddle()

ll.displayFromStart()
ll.displayFromEnd()
