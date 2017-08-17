class BinaryMinHeap
  attr_reader :store, :prc

  def initialize(&prc)
    @store = []
    @prc = prc 
  end

  def count
    @store.length 
  end

  def extract
    @store[0], @store[-1] = @store[-1], @store[0]
    el = @store.pop 
    BinaryMinHeap.heapify_down(@store, 0)
    el 
  end

  def peek
  end

  def push(val)
    @store.push(val)
    @store = BinaryMinHeap.heapify_up(@store,count)
  end

  public
  def self.child_indices(len, parent_index)
    if parent_index* 2 + 2 < len 
      [parent_index * 2 + 1, parent_index* 2 + 2] 
    elsif parent_index* 2 + 1 < len 
      [parent_index*2 +1]
    else 
      return nil 
    end   
  end

  def self.parent_index(child_index)
    if child_index > 0 
      (child_index - 1)/2
    else 
      raise "root has no parent"
    end 
  end

  def self.heapify_down(array, parent_idx, len = array.length, &prc)
    parent_index = parent_idx
    
    child_index = BinaryMinHeap.child_indices(len,parent_index)
    if child_index && child_index.length == 2 
      if prc 
        if prc.call(array[child_index[0]], array[child_index[1]]) >= 0 
           min_child_index = child_index[1]
        else 
          min_child_index = child_index[0]
        end 
      else 
        if array[child_index[0]] > array[child_index[1]]
            min_child_index = child_index[1]
        else 
            min_child_index = child_index[0]
        end 
      end   
    elsif child_index
      min_child_index = child_index[0]

    else 
      min_child_index = nil 
    end 

    until !min_child_index
       if prc  
          if_statement = (prc.call(array[parent_index],array[min_child_index]) >= 0)
       else 
          if_statement = (array[parent_index] > array[min_child_index])
       end      

       if if_statement
            array[parent_index], array[min_child_index] = array[min_child_index], array[parent_index]
            parent_index = min_child_index
            child_index = BinaryMinHeap.child_indices(len,parent_index)
            if child_index && child_index.length == 2 
              if prc  
                if prc.call(array[child_index[0]], array[child_index[1]]) >= 0 
                   min_child_index = child_index[1]
                else 
                   min_child_index = child_index[0]
                end 
              else
                if array[child_index[0]] > array[child_index[1]]
                    min_child_index = child_index[1]
                else 
                    min_child_index = child_index[0]
                end 
              end 
            elsif child_index
              min_child_index = child_index[0]
            else 
              min_child_index = nil 
            end 
       else 
         break 
       end  
    end 
    array
  end

  def self.heapify_up(array, child_idx, len = array.length, &prc)
    
    result_arr = []

    array.each_with_index do |el, idx|
      result_arr.push(el)
      if idx == 0 
        next 
      end 

      parent_indice = BinaryMinHeap.parent_index(idx)
      inner_loop_index = idx

      until !parent_indice 
        if prc  
          if_statement = (prc.call(result_arr[parent_indice],result_arr[inner_loop_index]) >= 0)
        else 
          if_statement = (result_arr[parent_indice] > result_arr[inner_loop_index])
        end 

        if if_statement
            result_arr[parent_indice], result_arr[inner_loop_index] = result_arr[inner_loop_index], result_arr[parent_indice]

            inner_loop_index = parent_indice
          begin 
            parent_indice = BinaryMinHeap.parent_index(parent_indice)
          rescue 
            parent_indice = nil 
          end 
        else 
          break 
        end 
      end 
    end 

    result_arr
  end
end
