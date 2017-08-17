require_relative "heap"

class Array
  def heap_sort!
  	result_arr = BinaryMinHeap.new
  	sorted_arr = []
  	self.each do |el|
  		result_arr.push(el)
  	end 

  	until result_arr.count == 0 
  		sorted_arr.push(result_arr.extract) 
  	end 	


  	sorted_arr.each_with_index do |el,idx|
  		self[idx] = el
  	end 
  	self 
  end
end
