from typing import List
'''
    Constant space, linear time
'''


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False

        closers_needed = 0
        wild_available = 0
        wilds_used_to_close = 0

        for char_locked, char in zip(locked, s):
            if char_locked == '1':
                if char == '(':
                    closers_needed += 1
                elif char == ')':
                    if closers_needed:
                        closers_needed -= 1
                    elif wilds_used_to_close:
                        wilds_used_to_close -= 1
                        wild_available += 1
                    elif wild_available:
                        wild_available -= 1
                    else:
                        return False
            else:
                if closers_needed:
                    wilds_used_to_close += 1
                    closers_needed -= 1
                else:
                    wild_available += 1

        return not closers_needed

