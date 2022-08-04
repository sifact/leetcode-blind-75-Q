class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def print_tree(self):
        elements = []

        if self.left:
            elements += self.left.print_tree()

        elements.append(self.data)

        if self.right:
            elements += self.right.print_tree()

        return elements

    # dfs
    def max_depth(self, root):

        if not root:
            return 0

        left = self.max_depth(root.left)
        right = self.max_depth(root.right)

        if left > right:
            return left + 1
        return right + 1

    # bfs
    def max_depth2(self, root):
        if not root:
            return 0

        q = []
        q.append(root)
        depth = 0
        while q:
            depth += 1
            tmp = []

            for node in q:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            q = tmp

        return depth


tree = BinaryTreeNode(3)
tree.left = BinaryTreeNode(9)
tree.right = BinaryTreeNode(20)
tree.right.left = BinaryTreeNode(15)
tree.right.right = BinaryTreeNode(7)
print(tree.print_tree())
print(tree.max_depth2(tree))

