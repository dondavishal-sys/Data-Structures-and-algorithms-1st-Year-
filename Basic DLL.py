class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
        self.prev = None

node1 = Node(10)
node2 = Node(20)
node1.next = node2 
node2.prev = node1

print(node1.next.data)
print(node2.prev.data)
