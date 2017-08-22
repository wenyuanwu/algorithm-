class QuickSort
  # Quick sort has average case time complexity O(nlogn), but worst
  # case O(n**2).

  # Not in-place. Uses O(n) memory.
  def self.sort1(array)
  end

  # In-place.
  def self.sort2!(array, start = 0, length = array.length, &prc)

    prc = prc || Proc.new { |el1, el2| el1 <=> el2 }

    return array if length < 2 
    # puts "array-main-before", array
    # puts "start", start 
    # puts "length", length
    splitpoint = QuickSort.partition(array,start,length, &prc)
    # puts "splitpoint", splitpoint
    # puts "array-main-aft", array
    QuickSort.sort2!(array,start,splitpoint - start, &prc)
    QuickSort.sort2!(array,splitpoint +1, start + length - splitpoint -1, &prc)
  end

  def self.partition(array, start, length, &prc)

    prc = prc || Proc.new { |el1, el2| el1 <=> el2 }
    # puts "initial_array", array
    pivot_val = array[start]
    # puts "pivot_val", pivot_val
    left_mark = start + 1 
    # puts "ini_left_mark", left_mark
    right_mark = start + length - 1 
    # puts "ini_right_mark", right_mark

    # (left_mark..right_mark).each do |idx|
    #   val = array[idx]
    #   if prc.call(pivot_val,val) < 1 
    # end 

    done = false 
    while !done 
      while left_mark <= right_mark && prc.call(array[left_mark],pivot_val) <= 0 
          left_mark += 1 
      end 
          # puts "left_mark", left_mark
      while prc.call(array[right_mark],pivot_val) > 0 && right_mark >= left_mark
          right_mark -= 1 
      end 

      if right_mark >= left_mark
        array[right_mark], array[left_mark] = array[left_mark], array[right_mark]
      else
          done = true
      end 
    end

    # puts "right_mark", right_mark
    # puts "start", start 
    # puts "array", array
    array[right_mark], array[start] = array[start], array[right_mark]
    # puts "array-after_swap", array
    return right_mark
  end

end
