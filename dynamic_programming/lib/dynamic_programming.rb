class DynamicProgramming

  def initialize
    @blair_cache = { 1 => 1, 2 => 2}
    @frog_cache = {}
    @super_frog_cache = {}
  end

  def blair_nums(n)

    if @blair_cache[n]
      return @blair_cache[n]
    else
      @blair_cache[n] = blair_nums(n -1) + blair_nums(n-2) + (n-1)*2 - 1
      return @blair_cache[n]
    end 
  end

  def frog_hops_bottom_up(n)
    cache = frog_cache_builder(n)
    cache[n]
  end

  def frog_cache_builder(n)
    cache = { 1 => [[1]], 2 => [[1,1],[2]], 3 => [[1,1,1],[1,2],[2,1],[3]]} 
    return cache if n < 4 
    (4..n).each do |i|
      step_one = cache[i-1].map{|arr| arr + [1]}
      step_two = cache[i-2].map{|arr| arr + [2]}
      step_three = cache[i-3].map{|arr| arr +[3]}
      cache[i] = step_one + step_two + step_three
    end
    cache   
  end

  def frog_hops_top_down(n)
    if @frog_cache[n]
      return @frog_cache[n]
    else
      @frog_cache[n] = frog_hops_top_down_helper(n)
      return @frog_cache[n]
    end  
  end

  def frog_hops_top_down_helper(n)
    if n == 1 
      return [[1]]
    elsif n == 2 
      return [[1,1],[2]]
    elsif n == 3 
      return [[1,1,1],[1,2],[2,1],[3]]
    else 
      step_one = frog_hops_top_down(n-1).map{|arr| arr + [1]}
      step_two = frog_hops_top_down(n-2).map{|arr| arr + [2]}
      step_three = frog_hops_top_down(n-3).map{|arr| arr +[3]}
      return step_one + step_two + step_three
    end 
  end

  def super_frog_hops(n, k)
    if k >= n 
      return frog_hops_bottom_up(n) 
    elsif @super_frog_cache[n]
      return @super_frog_cache[n]
    else 
      @super_frog_cache[n] = super_frog_helper(n,k)
      return @super_frog_cache[n]
    end 
  end

  def super_frog_helper(n,k)
    result_arr = [] 
    (1..k).each do |i|
      result_arr += super_frog_hops(n -i, k).map{|arr| arr + [i]}
    end 
    return result_arr
  end 

  def knapsack(weights, values, capacity)

  end

  # Helper method for bottom-up implementation
  def knapsack_table(weights, values, capacity)

  end

  def maze_solver(maze, start_pos, end_pos)
  end
end
