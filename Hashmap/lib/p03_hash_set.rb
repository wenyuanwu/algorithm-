require_relative 'p02_hashing'

class HashSet
  attr_reader :count

  def initialize(num_buckets = 8)
    @store = Array.new(num_buckets) { Array.new }
    @count = 0
  end

  def insert(key)
    @count += 1
    if @count > num_buckets
      resize! 
    end 
    self[key.hash].push(key) 
  end

  def include?(key)
    self[key.hash].include?(key)
  end

  def remove(key)
    @count -= 1
    self[key.hash].delete(key)
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
