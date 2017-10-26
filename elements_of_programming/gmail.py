class Link:
	def __init__(self, value = None, prev = None, n = None):
		self.value = value
		self.prev = prev
		self.n = n
	def __str__(self):
		print(self.value)
		print(self.prev)
		print(self.n)

class LinkedList:
	def __init__(self):
		self.head = Link()
		self.tail = Link()
		self.head.next = self.tail
		self.tail.prev = self.head
		# self.length = 0  

	def insert_link(self, new_link):
		temp = self.tail.prev 
		temp.n = new_link
		new_link.n = self.tail
		self.tail.prev = new_link
		new_link.prev = temp

	def update_link(self, existing_link):
		temp = existing_link.prev
		temp.n = existing_link.n
		existing_link.n.prev = existing_link.prev
		self.insert_link(existing_link)

	def __str__(self):
		result = ""
		current_node = self.head.n
		while current_node.value:
			subresult = "value: {} ".format(current_node.value)
			result += subresult
			current_node = current_node.n
		print(result)	

class Gmail:
	def __init__(self):
		self.conversation = {}
		self.linkedlist = LinkedList()

	def head(self):
		return self.linkedlist.head 

	def tail(self):
		return self.linkedlist.tail 
	
	def newMessage(self, conversationId, messageId):
		if conversationId not in self.conversation:
			newLink = Link({"message": [messageId], "conversation": conversationId})
			self.conversation[conversationId] = newLink
			self.linkedlist.insert_link(newLink)
		else: 
			existing_link = self.conversation[conversationId]
			value = existing_link.value
			value['message'].append(messageId)
			self.linkedlist.update_link(existing_link)

	def getConversations(self):
		# return self.tail.prev.value
		current_node = self.linkedlist.tail.prev
		result = ""
		count = 0 
		while current_node.prev and count < 26:
			subresult = "value: {} ".format(current_node.value)
			result += subresult
			current_node = current_node.prev
			count += 1
		return result
		# why return self.tail.prev doesn't work

# Linkedlist unit test
# l1 = Link(1)
# l2 = Link(2)
# l3 = Link(3)
# # l.__str__()
# list = LinkedList()
# list.insert_link(l1)
# list.insert_link(l2)
# list.insert_link(l3)
# list.update_link(l1)
# list.update_link(l3)
# list.__str__()

g = Gmail()
g.newMessage(1,1)
print(g.getConversations())
g.newMessage(2,2)
print(g.getConversations())
g.newMessage(3,3)
print(g.getConversations())
g.newMessage(1,4)
print(g.getConversations())
g.newMessage(3,5)
print(g.getConversations())
g.newMessage(1,100)
print(g.getConversations())


# newMessage(conversationId, messageId)
# getConversations(conversationId)

# converstion -> massages 

# create - > new Messages -> add message to conversation 


# HashMap {conversationId : {messages: (messageId)}, node: pointer}

# Linkedlist track the most recent conversation 

