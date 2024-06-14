class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        nums.append(nums[-1]+len(nums))
        moves = 0
        dups = []
        for a, b in pairwise(nums):
            differential = b-a
            if differential == 0:
                dups.append(b)
            else:
                available_nums = range(a+1, b)
                for num in available_nums:
                    if not dups:
                        break
                    moves += num - dups.pop()
        return moves
