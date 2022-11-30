from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        candidates = {person for person in range(1, n+1)}
        for truster, _ in trust:
            candidates.discard(truster)
        if len(candidates) != 1:
            return -1

        left_to_trust = {person for person in range(1,n+1)}
        candidate = candidates.pop()
        left_to_trust.discard(candidate)
        for truster, trusted in trust:
            if trusted == candidate:
                left_to_trust.discard(truster)

        return candidate if not left_to_trust else -1



# print(Solution())
