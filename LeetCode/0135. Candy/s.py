from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        def compare_to_previous_child():
            for child in range(1, len(ratings)):
                prev_child = child - 1
                if ratings[child] > ratings[prev_child]:
                    candies[child] = max(candies[child], candies[prev_child] + 1)

        compare_to_previous_child()
        candies = [*reversed(candies)]
        ratings = [*reversed(ratings)]
        compare_to_previous_child()
        return sum(candies)


print(Solution().candy([1,3,4,5,2]))
