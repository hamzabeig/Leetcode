class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        indegree = [0] * n
        ans = []

        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            adj[prerequisite].append(course) #index is prerequisite, list is courses
            indegree[course] += 1

        queue = deque()
        for i in range(n):
            if indegree[i] == 0: #start taking courses with no prerequisites
                queue.append(i)

        while queue:
            current = queue.popleft()
            ans.append(current)

            for next_course in adj[current]: #BFS to remove course's dependencies
                indegree[next_course] -= 1 #next course has one dependency removed
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return len(ans) == n #in the end, all courses must be finished
