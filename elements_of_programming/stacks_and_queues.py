# 8.1 implement a stack with max API
import collections

class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCacheMax', ('element', 'max'))

    def __init__(self):
        self._element_with_cached_max =[]

    def empty(self):
    	return len(self._element_with_cached_max) == 0 

    def max(self):
    	if self.empty():
    	    raise IndexError('max(): empty stack')
    	return self._element_with_cached_max[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._element_with_cached_max.pop().element

    def push(self, x):
        self._element_with_cached_max.append(self.ElementWithCachedMax(x, x if self.empty() else max(x, self.max())))	

stack_test = Stack()
print(stack_test)
print(stack_test.empty())
stack_test.push(10)
stack_test.push(4)
stack_test.push(15)
print(stack_test.max())
stack_test.pop()
print(stack_test.max())
stack_test.pop()
print(stack_test.max())


