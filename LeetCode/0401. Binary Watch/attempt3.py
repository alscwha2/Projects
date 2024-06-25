from typing import List
from collections import defaultdict
from itertools import combinations, product


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hours = defaultdict(list, {i : [str(sum(comb)) for comb in combinations((2**j for j in range(4)), i) if sum(comb) < 12] for i in range(4)})
        minutes = defaultdict(list, {i : [str(sum(comb)).zfill(2) for comb in combinations((2**j for j in range(6)), i) if sum(comb) < 60] for i in range(6)})
        return [":".join((hour, minute)) for i in range(turnedOn+1) for hour, minute in product(hours[i], minutes[turnedOn-i])]

