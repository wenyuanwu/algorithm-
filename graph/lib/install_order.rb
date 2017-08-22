# Given an Array of tuples, where tuple[0] represents a package id,
# and tuple[1] represents its dependency, determine the order in which
# the packages should be installed. Only packages that have dependencies
# will be listed, but all packages from 1..max_id exist.

# N.B. this is how `npm` works.

# Import any files you need to

require_relative 'graph'
require_relative 'topological_sort'

def install_order(arr)

	max = arr[0][0]
	vertex_arr = [] 
	edge_arr = Hash.new 

	arr.each do |el|
		if el.first > max 
			max = el.first
		end 
		if el.last > max 
			max = el.last 
		end 
	end 

	max.times do |i|
		vertex_arr[i+1] = Vertex.new(i+1)
		puts "vertex_arr[#{i+1}]", vertex_arr[i+1]
		puts "vertex_arr[#{i+1}].value", vertex_arr[i+1].value 
	end 

	arr.each do |el|
		Edge.new(vertex_arr[el.first], vertex_arr[el.last])
	end 



	max.times do |i|
		puts "vertex_arr[#{i+1}].in_edges", vertex_arr[i+1].in_edges 
	end 

	topological_sort(vertex_arr)
end
