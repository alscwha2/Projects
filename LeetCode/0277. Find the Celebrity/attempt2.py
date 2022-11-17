# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity_candidate = n - 1
        for person in range(n - 1):
            if not knows(person, celebrity_candidate):
                celebrity_candidate = person

        for person in range(celebrity_candidate):
            if not knows(person, celebrity_candidate) or knows(celebrity_candidate, person):
                return -1
        for person in range(celebrity_candidate + 1, n):
            if not knows(person, celebrity_candidate) or knows(celebrity_candidate, person):
                return -1
        return celebrity_candidate
