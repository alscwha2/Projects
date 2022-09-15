class Solution:
    def countAndSay(self, n: int) -> str:
        previous_string = "1"

        for _ in range(n - 1):
            current_string = ""

            current_digit = previous_string[0]
            count = 0
            for digit in previous_string:
                if digit != current_digit:
                    current_string += str(count) + current_digit
                    current_digit = digit
                    count = 0
                count += 1
            current_string += str(count) + current_digit

            previous_string = current_string

        return previous_string

print(Solution().countAndSay(4))