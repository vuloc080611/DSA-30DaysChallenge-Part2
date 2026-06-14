class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visited = {}
        def dfs(original):
            if original in visited:
                return visited[original]
            copy = Node(original.val)
            visited[original] = copy
            for neighbor in original.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)

# Test
if __name__ == "__main__":
    n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
    n1.neighbors = [n2,n4]; n2.neighbors = [n1,n3]; n3.neighbors = [n2,n4]; n4.neighbors = [n1,n3]
    s = Solution()
    clone = s.cloneGraph(n1)
    print(clone.val)  # 1
