from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_order = []

        # construct the adjacency list for the graph and the transpose
        prereqs = [set() for _ in range(numCourses)]
        postreqs = [set() for _ in range(numCourses)]

        for course, prereq in prerequisites:
            prereqs[course].add(prereq)
            postreqs[prereq].add(course)

        # find all of the courses that don't have prereqs
        courses_with_no_remaining_prereqs = []
        for node in range(numCourses):
            if len(prereqs[node]) == 0:
                courses_with_no_remaining_prereqs.append(node)

        # take a course, remove as a prereq requirement from all it's postreqs
        while courses_with_no_remaining_prereqs:
            node = courses_with_no_remaining_prereqs.pop()
            course_order.append(node)
            for course in postreqs[node]:
                prereqs[course].remove(node)
                if len(prereqs[course]) == 0:
                    courses_with_no_remaining_prereqs.append(course)

        # if you have taken all the courses return them, else []
        return course_order if len(course_order) == numCourses else []
