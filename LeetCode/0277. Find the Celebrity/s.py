# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity_candidate = n - 1
        for person in range(n - 1):
            if not knows(person, celebrity_candidate):
                celebrity_candidate = person

        return celebrity_candidate \
            if all(
                        knows(person, celebrity_candidate)
                and not knows(celebrity_candidate, person)
                   for person in range(n)
                        if person != celebrity_candidate)\
            else -1
