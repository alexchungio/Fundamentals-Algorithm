#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        res = []
        path = []
        
        # The target node is the last node in the graph.
        target_node = len(graph) - 1

        def dfs(graph, target_node, start_node):

            path.append(start_node)

            if start_node == target_node:
                # # Append a copy of the current path.
                # Use path[:] because path will be modified during backtracking.
                res.append(path[:])
                # backtraking
                # Remove the current node before returning.
                # Restore the previous state.
                path.pop()
                return
            
            for node in graph[start_node]:
                # Choose the next node and continue DFS search.
                dfs(graph, target_node, node)

            # Backtracking:
            # Remove the current node from the path after exploring all choices.
            path.pop()

        dfs(graph, target_node, 0)

        return res
         
        
        
# @lc code=end

