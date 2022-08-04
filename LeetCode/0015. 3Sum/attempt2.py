"""
Realized that I did a ton of extra work attempt1
1. Since the array was sorted, I didn't have to consider elements lower than i 
	because all of those sums were found previously
2. Therefore, if I wouldn't consider those elements, it would be guaranteed that num >= rest[i] >= rest[j]
	because the array is sorted
3. Took out of subroutine because why not, probably faster this way

Alternatively:
			while j < k:
				sum = nums[j] + nums[k]
				if sum == complement:
					sums.add((num, nums[j], nums[k]))
				if sum <= complement:
					j += 1
				if sum >= complement:
					k -= 1
This way is shorter but is a little slower because of extra comparisons, and not as clear
"""


class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		nums.sort()

		sums = set()
		for i in range(len(nums)):
			num = nums[i]
			if i is not 0 and num == nums[i-1]:
				continue

			complement = -num
			j = i + 1
			k = len(nums) - 1
			while j < k:
				sum = nums[j] + nums[k]
				if sum == complement:
					sums.add((num, nums[j], nums[k]))
					j += 1
					k -= 1
				elif sum < complement:
					j += 1
				elif sum > complement:
					k -= 1

		return [list(sum) for sum in sums]