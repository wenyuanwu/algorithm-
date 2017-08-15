# This class just dumbs down a regular Array to be statically sized.
class StaticArray

  def initialize(length) 
    @store = Array.new(length)
  end

  # O(1)
  def [](index)
    @store[index] 
  end

  # O(1)
  def []=(index, value)
    @store[index] = value
    @length = @store.length
  end

  def length 
    length = 0 
    @store.each do |el|
      if el 
        length += 1 
      end 
    end 
    length 
  end 

  protected
  attr_accessor :store

end
