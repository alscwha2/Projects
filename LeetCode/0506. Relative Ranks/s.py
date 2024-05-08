from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scores = [[points, athlete] for athlete, points in enumerate(score)]
        scores.sort(reverse=True)
        answer = [0] * len(scores)
        for i in range(len(scores)):
            place, athlete = scores[i]
            place = 0
            if i == 0:
                place = "Gold Medal"
            elif i == 1:
                place = "Silver Medal"
            elif i == 2:
                place = "Bronze Medal"
            else:
                place = str(i+1)
            answer[athlete] = place
        return answer

