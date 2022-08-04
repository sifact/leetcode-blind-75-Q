class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def inorder_traversal(self, node):
        res = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(node)
        return res

    def kth_smallest_elements(self, root, k):
        return self.inorder_traversal(root)[k - 1]


tree = BinaryTreeNode(5)
tree.left = BinaryTreeNode(3)
tree.left.right = BinaryTreeNode(4)
tree.left.left = BinaryTreeNode(2)
tree.left.left.left = BinaryTreeNode(1)
tree.right = BinaryTreeNode(6)

print(tree.inorder_traversal(tree))
print(tree.kth_smallest_elements(tree, 3))

