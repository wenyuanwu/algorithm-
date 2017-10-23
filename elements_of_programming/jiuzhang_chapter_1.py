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
# print(arr.subsets(list_exp))
# time complexity ??? 

# strStr 
# For a given source string and a target string, you should output the first index(from 0) of target string in source string.
# If target does not exist in source, just return -1.
class Solution:
    def strStr(self, source, target):
        # write your code here
        if (source =="" or source) and target =="":
            return 0
        if not source or not target:
            return -1 
        start_index = -1
        i = 0
        while i < len(source):
            if source[i] == target[0]:
                start_index = i
                sub_string = True
                for j in range(len(target)):
                    if (i + j) > len(source) -1 or source[i + j] != target[j]:
                        sub_string = False
                    if not sub_string:
                        break
                if sub_string: 
                    return start_index
                i = i + j - 1
            i = i + 1
        return -1




