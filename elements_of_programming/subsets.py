class Solution:

	def subsets(self, nums):
		self.results = []
		self.search(nums, self.results, [],0)
		return self.results 

	def search(self, nums, result, subset, start_index):
		result.append(subset)
		for i in range(start_index, len(nums)):
			subset.append(nums[i])
			self.search(nums, result, subset, start_index + 1)
			subset.pop()



s = Solution()
arr = [1,2,3]

print (s.subsets(arr))