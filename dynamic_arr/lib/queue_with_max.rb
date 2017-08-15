# Implement a queue with #enqueue and #dequeue, as well as a #max API,
# a method which returns the maximum element still in the queue. This
# is trivial to do by spending O(n) time upon dequeuing.
# Can you do it in O(1) amortized? Maybe use an auxiliary storage structure?

# Use your RingBuffer to achieve optimal shifts! Write any additional
# methods you need.

require_relative 'ring_buffer'

class QueueWithMax
  attr_accessor :store

  def initialize
    @store = RingBuffer.new()
    @max = nil 
    @max_arr =[]
  end

  def enqueue(val)
    @store.push(val)
    if !@max || val > @max
      @max = val 
    end 
    # max(val)
    # else 
    #   @secondary_max  
    @store 
  end

  def dequeue
    el = @store.shift 
    # if el == @max 
    #   @max = @max_hash[self.length - 1]
    # end 
    el 
  end

  def max
    # @max_hash[@store.length - 1] = @max  
    # if @store[-1] > val 
    #   @max_arr << val 
    # elsif @max_arr[-1] < val  
    #   @max_arr[-1] = val 
    # end 
    @max
  end

  def length
    @store.length 
  end

end
