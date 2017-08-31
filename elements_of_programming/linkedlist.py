# Implement the node 
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

# node = Node(93)
# print(node.getData())
# print(node.getNext())	

class Linkedlist:
    def __init__(self):
        self.head = None

    def isempty(self):
        return self.head == None

    def insert(self, item):
        newnode = Node(item)
        newnode.setNext(self.head)
        self.head = newnode

    def size(self):
        current = self.head
        count = 0 
        while current:
            count += 1 
            current = current.getNext()
        return count

    def search(self,data):
        current = self.head
        while current != None:
            if current.getData() == data:
                break
            current = current.getNext()
        return current

    def remove(self, data):
        current = self.head
        prev_node = None
        while current != None:
            if current.getData() == data:
                break
            prev_node = current
            current = current.getNext()

        if current and prev_node:    
        	prev_node.setNext(current.getNext())
        elif current and prev_node == None:
            self.head = current.getNext()    
        	

# nodelist = Linkedlist()
# print(nodelist.isempty())
# print(nodelist.size())
# nodelist.insert(3)
# nodelist.insert(5)
# print(nodelist.size())
# print(nodelist.search(3))
# print(nodelist.search(5))
# nodelist.remove(0)
# print(nodelist.size())

# 7.1 merge two sorted lists
def merge_two_sorted_list(L1,L2):
    dummy_node = tail = Node()
    pointer1 = L1.head
    pointer2 = L2.head
    while pointer1 and pointer2:
        if pointer1.getData() < pointer2.getData():
            tail.next, pointer1 = pointer1, pointer1.getNext()
        else:
            tail.next, pointer2 = pointer2, pointer2.getNext()
        tail = tail.next
    tail.next = pointer1 or pointer2

    return dummy_node.next

# L1 = Linkedlist()
# L1.insert(5)
# L1.insert(3)
# L1.insert(1)
# L2 = Linkedlist()
# L2.insert(4)
# L2.insert(2)
# L = merge_two_sorted_list(L1,L2)
# print(L.getData())

