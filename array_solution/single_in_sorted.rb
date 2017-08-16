def single_in_sorted(arr)
	mid = arr.length / 2 
	return nil if arr.length < 3 
	return arr[mid] if arr[mid + 1] != arr[mid] && arr[mid - 1] != arr[mid]
	if arr[mid] == arr[mid + 1]
		single_in_sorted(arr[mid+2..-1])
	else 
		single_in_sorted(arr[0..mid-2])
	end 
end

# arr = [1,1,2,2,3] - find the single element in a sorted arr  
# O(logn) - binary search 
# O(1) - space complexity # use while function rather than recursive function 