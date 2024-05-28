from typing import List

'''
        whenever you are going up, you are going up a mountain

        when you are going down, you are either:
        1 - going down a mountain
        2- going down something that isn't a mountain

        if b > a:
            if not going_up_mountain:
                foot_of_mountain = a
                going_up_mountain = True
        elif b < a:
            if not going_up_mountain and not going_down_mountain:
                continue
            if going_down_mountain:
                pass
            if going_up_mountain:
                going_down_mountain = True
                going_up_mountain = False
            current_mountain_length = b - foot_of_mountain
            longest  = max(longest, current)
        elif b == a:
            going_up_mountain = False
            going_down_mountain = False
'''

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        longest_mountain_length = 0
        foot_of_mountain = 0
        going_down_mountain = False
        going_up_mountain = False

        for b in range(1, len(arr)):
            a = b-1
            if arr[b] > arr[a]:
                if not going_up_mountain:
                    foot_of_mountain = a
                    going_up_mountain = True
            elif arr[b] < arr[a]:
                if not going_up_mountain and not going_down_mountain:
                    continue
                longest_mountain_length = max(longest_mountain_length, b - foot_of_mountain + 1)
                if going_up_mountain:
                    going_down_mountain = True
                    going_up_mountain = False
            elif arr[b] == arr[a]:
                going_up_mountain = False
                going_down_mountain = False
        return longest_mountain_length


