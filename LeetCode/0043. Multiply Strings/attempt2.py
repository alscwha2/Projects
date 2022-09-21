from itertools import starmap, product


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        first = [(num, len(num1) - i) for i, num in enumerate(num1, 1)]
        second = [(num, len(num2) - i) for i, num in enumerate(num2, 1)]

        third = [*starmap(lambda a, b: (int(a[0]) * int(b[0]), a[1] + b[1]), product(first, second))]
        total = [0] * (third[0][1] + 1)
        for num, zeroes in third:
            total[len(total) - zeroes - 1] += num
        for i in range(len(total)-1, 0, -1):
            tens, total[i] = divmod(total[i], 10)
            total[i - 1] += tens

        return ''.join(str(num) for num in total)

print(Solution().multiply("12345", "45678"))
