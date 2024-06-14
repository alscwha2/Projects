class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        nums.append(nums[-1]+len(nums))
        needed_numbers = 0
        added_num_sum = 0
        dup_sum = 0
        for a, b in pairwise(nums):
            differential = b-a
            if differential == 0:
                dup_sum += b
                needed_numbers += 1
            else:
                nums_to_take = min(needed_numbers, differential-1)
                added_num_sum += nums_to_take * (nums_to_take+1) // 2 + nums_to_take * a
                needed_numbers -= nums_to_take
        return added_num_sum - dup_sum
