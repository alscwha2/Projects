class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		def find3sumsForElement(num: int, rest: List[int]) -> List[tuple]:
			complement = -1 * num
			i = 0
			j = len(rest) - 1
			pairs = []
			while i < j:
				if rest[i] + rest[j] == complement:
					triplet = [num, rest[i], rest[j]]
					triplet.sort()
					pairs.append(tuple(triplet))
					i += 1
					j -= 1
				elif rest[i] + rest[j] < complement:
					i += 1
				elif rest[i] + rest[j] > complement:
					j -= 1
			return pairs

		nums.sort()

		sums = set()
		for i in range(len(nums)):
			num = nums[i]
			if i is not 0 and num == nums[i-1]:
				continue

			rest = nums[:i] + nums[i+1:]

			sums.update(find3sumsForElement(num, rest))

		returnlist = []
		for sum in sums:
			returnlist.append(list(sum))
		return returnlist