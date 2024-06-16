from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [''] * n
        for i in range(1, n+1):
            if not i % 3:
                answer[i-1] += 'Fizz'
            if not i % 5:
                answer[i-1] += 'Buzz'
            if not answer[i-1]:
                answer[i-1] = str(i)
        return answer
