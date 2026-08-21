class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            indegree[course] += 1
            adj[prereq].append(course)
        
        queue = deque()

        for course, prereqs in enumerate(indegree):
            if prereqs == 0:
                queue.append(course)
        
        processed_courses = 0
        while queue:
            prereq = queue.popleft()
            processed_courses += 1

            for next_course in adj[prereq]:
                indegree[next_course] -= 1
                    
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        if numCourses == processed_courses:
            return True
        else:
            return False

