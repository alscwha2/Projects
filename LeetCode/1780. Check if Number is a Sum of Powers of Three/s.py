class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
            convert to base 3
            make sure that there are no 2s
        """
        powers = [1, 3]
        while powers[-1] <= n:
            powers.append(powers[-1] * 3)
        for power in reversed(powers):
            if power <= n:
                n -= power
                if power <= n:
                    return False
        return True
