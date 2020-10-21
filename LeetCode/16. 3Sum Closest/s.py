class Solution:
	def threeSumClosest(self, nums: List[int], target: int) -> int:
		nums.sort()

		closest_value = nums[0] + nums[1] + nums[2]
		distance = abs(target - closest_value)
		for i in range(len(nums)):
			j = i + 1
			k = len(nums) - 1

			new_target = target - nums[i]

			while j < k:
				current_distance = new_target - nums[j] - nums[k]
				if current_distance == 0:
					return target
				if abs(current_distance) < distance:
					distance = abs(current_distance)
					closest_value = nums[i] + nums[j] + nums[k]
				if current_distance > 0:
					j += 1
				if current_distance < 0:
					k -= 1
		return closest_value