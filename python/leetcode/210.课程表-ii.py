#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # DAG （Directed Acyclic Graph）
        # Topological Sorting (Kahn's Algorithm)
        
        # build the adjacency list of the directed graph
        graph = collections.defaultdict(list)
        
        # indegree[i] represents the number of prerequisites
        # that course i still needs
        indegree = [0] * numCourses
        
        # Store the topological ordering of courses.
        studied = []

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
            # Add the current course to the learning order.
            studied.append(course)
            # update the indegree of its neighbors
            for next_coourse in graph[course]:
                indegree[next_coourse] -= 1
                
                # If all prerequisites have been satisfied,
                # the course can now be taken
                if indegree[next_coourse] == 0:
                    q.append(next_coourse)

        # If all courses have been processed,
        # return one valid topological ordering.
        # Otherwise, a cycle exists, so no valid ordering is possible.
        return studied if len(studied) == numCourses else []
    
# @lc code=end

