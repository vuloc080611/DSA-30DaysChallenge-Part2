class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        def dfs(node):
            if not node:
                vals.append('#')
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        vals = []
        dfs(root)
        return ','.join(vals)

    def deserialize(self, data):
        def dfs():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        vals = iter(data.split(','))
        return dfs()

if __name__ == "__main__":
    codec = Codec()
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    s = codec.serialize(root)
    print(s)
    new_root = codec.deserialize(s)
    print(new_root.val)  # 1
