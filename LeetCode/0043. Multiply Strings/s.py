from itertools import groupby, starmap
from functools import reduce


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        def my_product(first, second):
            if len(second) > len(first):
                first, second = second, first

            for i in range(len(first)):
                j = 0
                while i >= 0 and j < len(second):
                    yield first[i], second[j]
                    i, j = i - 1, j + 1

            for j in range(1 + (len(first) - len(second)), len(second)):
                i = len(first) - 1
                while i >= 0 and j < len(second):
                    yield first[i], second[j]
                    i, j = i - 1, j + 1

        first = [(num, len(num1) - i) for i, num in enumerate(num1, 1)]
        second = [(num, len(num2) - i) for i, num in enumerate(num2, 1)]

        third = [*starmap(lambda a, b: (int(a[0]) * int(b[0]), a[1] + b[1]), my_product(first, second))]
        total = [reduce(lambda a, b: a + b[0], group[1], 0) for group in groupby(third, key=lambda a: a[1])]
        for i in range(len(total)-1, 0, -1):
            tens, total[i] = divmod(total[i], 10)
            total[i - 1] += tens

        return ''.join(str(num) for num in total)

print(Solution().multiply("31", "121"))
