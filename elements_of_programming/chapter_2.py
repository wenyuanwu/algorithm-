class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def findPosition(self, A, target):
        # Write your code here
        print(len(A), "len(A)")
        print(A, "A")

        if len(A) == 0 or A == None:
            return -1
            
        mid_idx = int(len(A)/2)
        left_arr = A[:mid_idx]
        if mid_idx + 1 < len(A):
            right_arr = A[mid_idx + 1:]
        else:
            right_arr = []
        
        if A[mid_idx] == target:
            return mid_idx
        elif A[mid_idx] > target:
            return self.findPosition(left_arr, target)
        else:
            if self.findPosition(right_arr, target) > 0:
                return mid_idx + 1 + self.findPosition(right_arr, target)
            
arr = Solution()
list_exp = [1, 2, 2, 4, 5, 5]
print(arr.findPosition(list_exp, 6))
