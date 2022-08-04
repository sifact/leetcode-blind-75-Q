class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def preorder_traversal(self, root):
        elements = []

        elements.append(str(root.val))
        if root.left:
            elements += self.preorder_traversal(root.left)

        if root.right:
            elements += self.preorder_traversal(root.right)

        return elements

    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append('N')
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        vals = data.split()
        self.i = 0

        def dfs():
            if vals[self.i] == 'N':
                self.i += 1
                return

            node = BinaryTreeNode(int(vals[self.i]))
            node.left = dfs()
            node.right = dfs()
            return node


tree = BinaryTreeNode(1)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(3)
tree.right.left = BinaryTreeNode(4)
tree.right.right = BinaryTreeNode(5)


print(tree.preorder_traversal(tree))
print(tree.serialize(tree))
