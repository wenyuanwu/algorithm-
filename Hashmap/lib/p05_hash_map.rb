require_relative 'p02_hashing'
require_relative 'p04_linked_list'

class HashMap
  attr_reader :count
  include Enumerable
  
  def initialize(num_buckets = 8)
    @store = Array.new(num_buckets) { LinkedList.new }
    @count = 0
  end

  def include?(key)
    each {|node| return true if node.first == key}
    return false 
  end

  def set(key, val)
    if @store[bucket(key.hash)].include?(key)
      @store[bucket(key.hash)].update(key, val)
    else 
      @count += 1
      if @count > num_buckets
        resize!
      end 
      @store[bucket(key.hash)].append(key, val)
    end 
  end

  def get(key)
    @store[bucket(key.hash)].get(key)
  end

  def delete(key)
     @count -= 1 
     @store[bucket(key.hash)].remove(key)   
  end

  def each
    @store.each do |linked_list|
      linked_list.each {|node| yield [node.key, node.val]}
    end 
  end

  # uncomment when you have Enumerable included
  # def to_s
  #   pairs = inject([]) do |strs, (k, v)|
  #     strs << "#{k.to_s} => #{v.to_s}"
  #   end
  #   "{\n" + pairs.join(",\n") + "\n}"
  # end

  alias_method :[], :get
  alias_method :[]=, :set

  private

  def num_buckets
    @store.length
  end

  def resize!
    @new_store = Array.new(num_buckets* 2) { LinkedList.new }
    @store.each do |linked_list|
        linked_list.each do |node|
          @new_store[bucket(node.key.hash)].append(node.key, node.val)
        end 
    end 
    @store = @new_store
  end

  def bucket(key)
    # optional but useful; return the bucket corresponding to `key`
      key % num_buckets
  end
end
