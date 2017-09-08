# subsets of array with distinct integer

class Solution:
    """
    @param: nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        if nums == []:
            return [[]]
        nums.sort()
        result = []
        subset = []
        self.helper(result, nums, 0, subset)
        return result 
    
    def helper(self,result, nums, start_index, subset):
        # print(result,"result-before")
        # print(subset,"subset-outer")
        result.append(list(subset))
        # print(result,"result-after")
        for i in range(start_index, len(nums)):
            # print(subset,"subset-inner-before")
            subset.append(nums[i])
            # print(subset,"subset-inner-after")
            self.helper(result, nums, i + 1, subset)
            subset.pop()

arr = Solution()
list_exp = [3,2,1]
print(arr.subsets(list_exp))