class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
   
def is_balanced(tree_root):    
    if tree_root is None:
        return True      
    depths = []
    nodes = []
    nodes.append((tree_root, 0))
        
    while len(nodes):   
        node, depth = nodes.pop()
        if not node.left and not node.right:
            if depth not in depths:
                depths.append(depth)
                print(depths)
                if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                    return False 
        if node.left:
            nodes.append((node.left, depth + 1))
        if node.right:
            nodes.append((node.right, depth + 1))

    return True
                  
        
# run your function through some test cases here
# remember: debugging is half the battle!
root = BinaryTreeNode(1)
first_left = root.insert_left(2)
root.insert_right(3)
second_left = first_left.insert_left(4)
third_left = second_left.insert_left(6)
print (is_balanced(root))
