class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            indegree[course] += 1
            adj[prereq].append(course)

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        processed_courses = 0

        while queue:
            course = queue.popleft()
            processed_courses += 1

            for next_course in adj[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        return processed_courses == numCourses