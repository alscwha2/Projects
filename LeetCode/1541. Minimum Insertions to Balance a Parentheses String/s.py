from typing import List
'''
    Iterate through the string:
    1 - Keep track of how many closers (i.e. ')') are needed to close 
        all of the openers (i.e. '(') that have been seen.
    2 - If you find too many closers, then there must be missing openers
    3 - Since closers come in pairs, you need to keep track of the last 
        character that you have seen, and always evaluate the current 
        character in light of that. If you were expecting a closer and
        you find an opener, then there must be a missing closer.
'''

class Solution:
    def minInsertions(self, s: str) -> int:
        need_one_more_closer = False
        missing_openers = 0
        missing_closers = 0
        remaining_needed_closers = 0
        for char in s:
            if   char == '(':
                remaining_needed_closers += 2
                if need_one_more_closer:
                    missing_closers += 1
                    remaining_needed_closers -= 1
                    need_one_more_closer = False
            elif char == ')':
                if remaining_needed_closers == 0:
                    missing_openers += 1
                    remaining_needed_closers += 2
                remaining_needed_closers -= 1
                need_one_more_closer = not need_one_more_closer
        return missing_openers + missing_closers + remaining_needed_closers
