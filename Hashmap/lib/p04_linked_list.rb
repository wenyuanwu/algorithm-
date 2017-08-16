class Node
  attr_accessor :key, :val, :next, :prev

  def initialize(key = nil, val = nil)
    @key = key
    @val = val
    @next = nil
    @prev = nil
  end

  def to_s
    "#{@key}: #{@val}"
  end

  def remove
    # optional but useful, connects previous node to next node
    # and removes self from list.
    prev_node = self.prev 
    next_node = self.next
    prev_node.next = next_node
    next_node.prev = prev_node
  end

end

class LinkedList
  include Enumerable

  def initialize
    @head = Node.new
    @tail = Node.new
    @head.next = @tail
    @tail.prev = @head
  end

  def [](i)
    each_with_index { |node, j| return node if i == j }
    nil
  end

  def first
    @head.next
  end

  def last
    @tail.prev

  end

  def empty?
    @head.next.next == nil
  end

  def get(key)
    each {|node| return node.val if node.key == key}
  end

  def include?(key)
    each do |node|
      if (node.key == key)
        return true
      end 
    end
    return false
  end

  def append(key, val)
    @new_node = Node.new(key,val)
    prev_node = @tail.prev
    @new_node.next = @tail
    @new_node.prev = prev_node
    prev_node.next = @new_node
    @tail.prev = @new_node
    
    @new_node
  end

  def update(key, val)
    each {|node| node.val = val if node.key == key}
  end

  def remove(key)
    each do |node|
      if (node.key == key)
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
       end  
    end
  end

  def each(&block)
    node = @head.next
    while node.next != nil 
      block.call(node)
      node = node.next
    end 
  end

  # uncomment when you have `each` working and `Enumerable` included
  def to_s
    inject([]) { |acc, node| acc << "[#{node.key}, #{node.val}]" }.join(", ")
  end
end
