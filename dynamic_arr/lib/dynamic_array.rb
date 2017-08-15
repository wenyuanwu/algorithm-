require_relative "static_array"

class DynamicArray
  attr_reader :length

  def initialize
    @capacity = 8 
    @store = StaticArray.new(capacity)
    @length = 0
  end

  # O(1)
  def [](index)
    if @store[index]
      @store[index]
    else 
      raise "index out of bounds"
    end 
  end

  # O(1)
  def []=(index, value)
    @store[index] = value
  end

  # O(1)
  def pop
    last_elm = self[@length -1]
    @store = @store[0...@length -1]
    @length = @store.length
    last_elm
  end

  # O(1) ammortized; O(n) worst case. Variable because of the possible
  # resize.
  def push(val)
    if @length == capacity
      resize!
    end 

    self[@length] = val
    @length = @store.length
  end

  # O(n): has to shift over all the elements.
  def shift
    first_elm = self[0]
    idx = 0 
    while idx < @length  
      @store[idx] = @store[idx + 1]
      idx += 1
    end 
    @length = @store.length
    first_elm
  end

  # O(n): has to shift over all the elements.
  def unshift(val)
    if @length == capacity
      resize!
    end 

    idx = @length 
    while idx > 0 
      @store[idx] = @store[idx -1]
      idx -= 1 
    end     
    @store[0] = val

    @length = @store.length
  end

  protected
  attr_accessor :capacity, :store
  attr_writer :length

  def check_index(index)
    
  end

  # O(n): has to copy over all the elements to the new store.
  def resize!
    @capacity *= 2 
    @new_store = StaticArray.new(capacity)
    idx = 0 
    while idx < @length
      @new_store[idx] = @store[idx]
      idx += 1
    end 
    @store = @new_store
  end
end
