from typing import List
from itertools import combinations, product



class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        hours = defaultdict(list)
        for i in range(4):
            combs = combinations((2**j for j in range(4)), i)
            hours[i] = [str(sum(comb)) for comb in combs if sum(comb) < 12]

        minutes = defaultdict(list)
        for i in range(6):
            combs = combinations((2**j for j in range(6)), i)
            minutes[i] = [str(sum(comb)).zfill(2) for comb in combs if sum(comb) < 60]

        answer = []
        for i in range(turnedOn+1):
            answer.extend(':'.join(pair) for pair in product(hours[i], minutes[turnedOn-i]))

        return answer
