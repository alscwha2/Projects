from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List [int], k: int) -> bool:
        window_length = min(k+1, len(nums))

        seen = set(nums[:window_length])
        if len(seen) < window_length:
            return True

        for i in range(len(nums)-window_length):
            seen.remove(nums[i])
            if nums[i+window_length] in seen:
                return True
            seen.add(nums[i+window_length])
        return False
