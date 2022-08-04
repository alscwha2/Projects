class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for num in nums:
            if target - num in seen:
                return [num, target - num]
            else:
                seen.add(num)
