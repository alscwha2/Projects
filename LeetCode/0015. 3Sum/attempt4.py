from typing import List
"""
Copying attempt2 but trying to use hashing for complement lookup
ABORTED!!!!
"""


class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		nums.sort()
		numset = set(nums)
		dupset = set([num for num in nums if nums.count(num) > 1])
		singlist = list(numset)
		singlist.sort()
		length = len(nums)

		sums = []
		
		# deal with all things zero
		if 0 in numset:
			numset.remove(0)
			if nums.count(0) >= 3:
				sums.append([0,0,0])
			for num in singlist:
				if num >= 0:
					continue
				if -num in numset:
					sums.append([num, 0, -num])

		# deal with all things not zero nor duplicate
		for i in range(len(singlist)):
			num = singlist[i]
			while j < len(singlist):
				othernum = singlist[j]
				complement = -num - othernum
				if complement == num or complement == othernum or complement not in numset:
					continue
				triple = [num, othernum, complement]
				triple.sort()
				sums.append(triple)
		# deal with duplicates
		for num in dupset:
			if -(num * 2) in numset:
				triple = [num, num, -(num * 2)] if num < 0 else [-(num * 2), num, num]
				sums.append(triple)

		return sums

print(Solution().threeSum([1,1,-2]))