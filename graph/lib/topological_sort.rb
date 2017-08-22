require_relative 'graph'

# Implementing topological sort using both Khan's and Tarian's algorithms

def sort(vertices)
	
	return [] if vertices.length == 0  

	list = []
	queue = [] 


	# puts "vertices.length-before", vertices.length
	vertices.each do |vertex|
		puts "vertex.value",vertex.value
		puts "vertex.in_edges",vertex.in_edges 
		queue.push(vertex) if vertex.in_edges == []
		# 
	end 

	# queue.each do |vertex|
		# puts "queue-ver-value", vertex.value 
	# end 
	# puts "queue.length", queue.length
	# puts "queue.first.value", queue.first.value if queue.first
	# puts "queue.first.out_edges", queue.first.out_edges if queue.first  
	return nil if queue.length == 0 

	while queue.length > 0 
		v = queue.pop
		# puts "v.value", v.value 
		if v 
			# puts "out_edges", v.out_edges
			while v.out_edges.length > 0 
				v.out_edges.pop.destroy! 
			end 
		end 

		list.push(v) if !list.include?(v)
	end 

	# puts "queue.later-on", queue
	# puts "list", list
	vertices = vertices.select {|vertex| !list.include?(vertex)}

	# vertices.each do |vertex|
		# puts "vertex-after", vertex.value
	# end 	
	# puts "vertices.length", vertices.length
	list.concat(sort(vertices))
end


def topological_sort(vertices)
	arr = sort(vertices)
	puts "arr", arr
	arr.each do |vert|
		puts "v", vert.value
	end 
	arr 
end 