class Solution:
	def maxArea(self, height: List[int]) -> int:
		# calculate end-to-end volume
		r = len(height) - 1
		l = 0
		best = 0

		while r > l:
			if height[r] > height[l]:
				current = height[l] * (r-l)
				l += 1
			else:
				current = height[r] * (r-l)
				r -= 1
			if current > best:
				best = current

		return best