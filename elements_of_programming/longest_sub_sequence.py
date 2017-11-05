import copy

class Solution:

	result_arr = []

	def longest_sub_sequence(self, arr):
		if not arr:
			return []
		self.result_arr = list([arr[0]])	
		self.helper([arr[0]], arr)
		return self.result_arr

	def helper(self, current_arr, arr):
		# print(result_arr,"result_arr")
		if len(current_arr) > 1 and current_arr[-1] <= current_arr[-2]:
			return
		if len(current_arr) > len(self.result_arr):
			# print(current_arr,"c")
			# print(result_arr,"r-b")
			self.result_arr = list(current_arr)
			# print(result_arr,"r-a")
		for i in range(1, len(arr)):
			current_arr.append(arr[i])
			self.helper(current_arr,arr[i:])
			current_arr.pop()


arr1 = []
arr2 = [2,5,1,3,4]
arr3 = [1, 3, 2, 3, 4, 8, 7, 9]
s = Solution()
# print(longest_sub_sequence(arr1))
print(s.longest_sub_sequence(arr2))
# print(s.longest_sub_sequence(arr3))