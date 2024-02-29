class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_removed = 0
        for index in range(1, len(nums)):
            if nums[index] == nums[index - num_removed - 1]:
                num_removed += 1
            nums[index - num_removed] = nums[index]
        return len(nums) - num_removed
