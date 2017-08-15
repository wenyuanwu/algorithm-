require_relative "static_array"

class RingBuffer
  attr_reader :length

  def initialize
    @capacity = 8 
    @store = StaticArray.new(capacity)
    @length = 0
    @start_idx = 0 
  end

  # O(1)
  def [](index)
    idx = check_index(index)
    if @store[idx]
      @store[idx]
    else 
      raise "index out of bounds"
    end 
  end

  # O(1)
  def []=(index, val)
    @store[index] = val
  end

  # O(1)
  def pop
    last_elm = self[@length -1]
    idx = check_index(@length -1)
    @store[idx] = nil 
    @length = @store.length
    last_elm
  end

  # O(1) ammortized
  def push(val)
    if @length == capacity
      resize!
    end 
    idx = check_index(@length)
    self[idx] = val
    @length = @store.length
  end

  # O(1)
  def shift
    first_elm = self[0]
    @store[@start_idx] = nil 
    @start_idx = (@start_idx + 1) % @capacity
    @length = @store.length
    first_elm
  end

  # O(1) ammortized
  def unshift(val)
    if @length == capacity
      resize!
    end 

    @start_idx = (@start_idx - 1) % @capacity   
    @store[@start_idx] = val
    @length = @store.length
  end

  protected
  attr_accessor :capacity, :start_idx, :store
  attr_writer :length

  def check_index(index)
    (@start_idx + index) % @capacity 
  end

  def resize!
    @new_store = StaticArray.new(@capacity*2)
    idx = @start_idx
    index = 0 
    while index < @length  
        @new_store[idx] = self[index] 
        idx += 1 
        index += 1 
    end   
    @store = @new_store
    @capacity *= 2 
    # only change the capacity after shifted to the new_store
  end
end
