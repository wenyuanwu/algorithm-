class MaxIntSet
  def initialize(max)
    @store = Array.new(max, false)
  end

  def insert(num)
    if num < @store.length && num > 0 
      @store[num] = true 
    else 
      raise 'Out of bounds'
    end
  end

  def remove(num)
    @store[num] = false 
  end

  def include?(num)
    @store[num] == true 
  end

  private

  def is_valid?(num)

  end

  def validate!(num)
  end
end


class IntSet
  def initialize(num_buckets = 20)
    @store = Array.new(num_buckets) { Array.new }
  end

  def insert(num)
    self[num].push(num)
  end

  def remove(num)
    self[num].delete(num)
  end

  def include?(num)
    self[num].include?(num)
  end

  private

  def [](num)
    # optional but useful; return the bucket corresponding to `num`
    @store[num % num_buckets]
  end

  def num_buckets
    @store.length
  end
end

class ResizingIntSet
  attr_reader :count

  def initialize(num_buckets = 20)
    @store = Array.new(num_buckets) { Array.new }
    @count = 0
  end

  def insert(num)
    @count += 1
    if @count > num_buckets
      resize! 
    end 
    self[num].push(num) 
  end

  def remove(num)
    @count -= 1
    self[num].delete(num)
  end

  def include?(num)
    self[num].include?(num)
  end

  private

  def [](num)
    # optional but useful; return the bucket corresponding to `num`
    @store[num % num_buckets]
  end

  def num_buckets
    @store.length
  end

  def resize!
    @new_store = Array.new(num_buckets* 2) { Array.new }
    @store.each do |arr|
        arr.each do |el|
          @new_store[el % (num_buckets * 2)].push(el)
        end 
    end 
    @store = @new_store
  end
end
