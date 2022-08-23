from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)

        def ksum(*, k, starting_index, target):
            groups = []

            if k > 2: # populate groups recursively
                previous = nums[starting_index] + 1
                for i, num in enumerate(nums[starting_index:len(nums)-(k-1)], starting_index):
                    if num == previous:
                        continue
                    for group in ksum(k=k-1, starting_index=i+1, target=target-num):
                        groups.append([num] + group)
                    previous = num

            elif k == 2: # populate groups of two by iteration
                l, r = starting_index, len(nums) - 1
                while l < r:
                    l_num, r_num = nums[l], nums[r]
                    current = l_num + r_num
                    if current == target:
                        groups.append([l_num, r_num])
                    if current >= target:
                        while nums[r] == r_num and l < r:
                            r -= 1
                    if current <= target:
                        while nums[l] == l_num and l < r:
                            l += 1

            else:
                raise ValueError("fourSum only valid for lists with 4 or more elements.")

            return groups # Last line of ksum function

        return ksum(k=4, starting_index=0, target=target)


print(Solution().fourSum([-3,-2,-1,0,0,1,2,3], 0))