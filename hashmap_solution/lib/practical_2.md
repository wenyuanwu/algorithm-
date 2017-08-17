## Problem
This is a two part problem:
1. First, write a series of instructions on how to build out an LRU Cache (pretend 
the person you're writing to has no idea how to build one. Don't forget to address
the reasoning behind using particular data structures).
2. Implement an LRU Cache from scratch with no outside references. **Don't look 
at the code or instructions from your homework!**

## Solution

### Part 1
Write first part here:
1. Utilize HashMap to track/access the Linkedlist 
2. Create Linkedlist to store the data 
3. If the key of the query doesn't exist, create new k-v pair and save it into the linkedlist and update the link in Hashmap 
4. If the query is with an exisiting key value, access the node of linkedlist through hashmap and return the value of the node. Also move the node to the end of the linkedlist (the closer to the tail, the more recent the query)
5. LRU has maximum memory, if the length of the linkedlist is beyond certain point, the node closest to the head is dropped  

### Part 2
```ruby
class LRUCache

	def initialize 
		@max = max 
		@map = HashMap.new 
		@store = LinkedList.new 
		@prc = prc 

	end 

	def get(key)
		if @store.includes(key)
			node = @map[key]
			move(node)
			node.val
		else 
			click!(key)	
		end 
	end 

	def count 
		@store.length 
	end 


	def click!(key)
		val = @prc.call(key)
		new_node = @store.append(key, val)
		map[key] = new_node 

		if count > @max 
			drop! 
		end 
	end 


	def drop! 
		first = @store.first 
		@store.remove(first)
		@map.remove(first.key)
	end 

	def move(node)
		@store.append(node.key, node.val)
		@map.remove(node.key)
	end 

end
```