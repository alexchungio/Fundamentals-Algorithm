#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # DAG （Directed Acyclic Graph）
        # Topological Sorting (Kahn's Algorithm)
        
        # build the adjacency list of the directed graph
        graph = collections.defaultdict(list)
        
        # indegree[i] represents the number of prerequisites
        # that course i still needs
        indegree = [0] * numCourses
        
        # Count how many courses have been completed
        studied = 0

        # Build the graph and calculate the indegree of each course
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        # Initialize the queue with all courses
        # that have no prerequisites
        q = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            course = q.popleft()
            # update the number os studied course
            studied += 1
            
            # update the indegree of its neighbors
            for next_coourse in graph[course]:
                indegree[next_coourse] -= 1
                
                # If all prerequisites have been satisfied,
                # the course can now be taken
                if indegree[next_coourse] == 0:
                    q.append(next_coourse)

        # If every course has been taken,
        # there is no cycle in the graph
        return studied == numCourses
        
        
# @lc code=end
