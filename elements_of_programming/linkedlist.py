# Implement the node 
class Node:
    def __init__(self, data):
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
        	

nodelist = Linkedlist()
print(nodelist.isempty())
print(nodelist.size())
nodelist.insert(3)
nodelist.insert(5)
print(nodelist.size())
print(nodelist.search(3))
print(nodelist.search(5))
nodelist.remove(0)
print(nodelist.size())
