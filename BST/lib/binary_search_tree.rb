# There are many ways to implement these methods, feel free to add arguments 
# to methods as you see fit, or to create helper methods.
require 'bst_node'

class BinarySearchTree
  attr_reader :root 

  def initialize
    @root = nil 
  end

  def insert(value, current_root = @root)
    if @root == nil 
      @root = BSTNode.new(value)
    elsif current_root.value >= value 
      if current_root.left == nil 
        current_root.left = BSTNode.new(value) 
      else 
        current_root = current_root.left 
        insert(value, current_root)
      end 
    else 
      if current_root.right == nil  
        current_root.right = BSTNode.new(value)
      else
        current_root = current_root.right 
        insert(value, current_root)
      end 
    end   
  end

  def find(value, tree_node = @root)
    return nil if tree_node == nil  

    return tree_node if tree_node.value == value 
    
    if tree_node.value > value 
      tree_node = tree_node.left
      find(value, tree_node)
    else
      tree_node = tree_node.right
      find(value,tree_node)
    end 
  end

  def delete(value)
    node = find(value)
    # puts "node.left", node.left
    # puts "node.left.value", node.left.value
    # puts "node.right", node.right
    # puts "node.right.value", node.right.value
    # puts "node.value", node.value

    # no-child
    if node.left == nil && node.right == nil 
      parent_node = find_parent(value)
      # puts parent_node.value,"parent_node.value"
      if parent_node == nil 
        @root = nil 
      elsif parent_node.left == node 
        parent_node.left = nil 
      else 
        parent_node.right = nil 
      end 
    else 
    # one-child  
      if node.left == nil && node.right 
        parent_node = find_parent(value)
        if parent_node.left == node 
          parent_node.left = node.right 
        else 
          parent_node.right = node.right
        end 
      elsif node.right == nil && node.left 
        parent_node = find_parent(value)
        if parent_node.left == node 
          parent_node.left = node.left 
        else 
          parent_node.right = node.left
        end 
      # two-children
      else 
        left_max = maximum(node.left)
        # puts "left_max", left_max.value
        parent_node = find_parent(value)
        parent_left_max = find_parent(left_max.value)
        # puts "parent_left_max", parent_left_max.value
        if parent_node.left == node 
          parent_node.left = left_max
        else 
          parent_node.right = left_max
        end 

        if(left_max.left)
          if parent_left_max.left = left_max
            parent_left_max.left = left_max.left
            left_max.left = node.left
          else 
            parent_left_max.right = left_max.left
            left_max.right = node.right 
          end 
        end 

      end  
    end    

  end

  # helper method for #delete:
  def maximum(tree_node = @root)
    while tree_node.right 
      tree_node = tree_node.right
    end 
    return tree_node
  end

  def depth(tree_node = @root)
    return 0 if tree_node == nil 
    return 0 if tree_node.left == nil && tree_node.right == nil 

    if tree_node.left == nil && tree_node.right 
      return  depth(tree_node.right) + 1 
    elsif tree_node.left && tree_node.right == nil 
      return depth(tree_node.left) + 1 
    elsif tree_node.right && tree_node.left 
      if  depth(tree_node.right) > depth(tree_node.left)
        return  depth(tree_node.right) + 1 
      else 
        return depth(tree_node.left) + 1 
      end 
    end 
  end 

  def is_balanced?(tree_node = @root)
    if tree_node.nil?
      return true 
    elsif tree_node.left == nil && tree_node.right == nil
      return true 
    elsif (depth(tree_node.left) - depth(tree_node.right)).abs > 1 
      return false 
    else 
      is_balanced?(tree_node.left) && is_balanced?(tree_node.right)
    end 
  end

  def in_order_traversal(tree_node = @root, arr = [])

  end


  private
  # optional helper methods go here:
  def find_parent(value, tree_node = @root)
    return nil if @root.value == value 
    # puts "tree_node.value", tree_node.value
    # puts "tree_node.left.value", tree_node.left.value
    # puts "tree_node.right.value", tree_node.right.value
    return tree_node if tree_node.left.value == value || tree_node.right.value == value 

    if tree_node.value > value 
      tree_node = tree_node.left
      find_parent(value, tree_node)
    else
      tree_node = tree_node.right
      find_parent(value,tree_node)
    end 

  end 

end
