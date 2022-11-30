from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        def people_who_do_not_trust_anyone():
            candidates = {person for person in range(1, n+1)}
            for truster, _ in trust:
                candidates.discard(truster)

            return candidates

        def everyone_trusts(candidate):
            left_to_trust = {person for person in range(1,n+1)}

            left_to_trust.discard(candidate)
            for truster, trusted in trust:
                if trusted == candidate:
                    left_to_trust.discard(truster)
            return left_to_trust

        candidates = people_who_do_not_trust_anyone()
        if len(candidates) != 1:
            return -1

        candidate = candidates.pop()

        return candidate if everyone_trusts(candidate) else -1



# print(Solution())
