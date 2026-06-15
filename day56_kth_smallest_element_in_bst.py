class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

# Test
if __name__ == "__main__":
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    s = Solution()
    print(s.kthSmallest(root, 1))  # 1
