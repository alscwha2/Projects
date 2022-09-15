class Solution:
    def countAndSay(self, n: int) -> str:
        def countAndSayOneString(previous_string: str):
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

            return current_string

        answer = "1"
        for _ in range(n - 1):
            answer = countAndSayOneString(answer)

        return answer

print(Solution().countAndSay(4))
