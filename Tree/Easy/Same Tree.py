class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def in_order_traversal(self, root):

        elements = []

        if root:
            elements += self.in_order_traversal(root.left)
            elements.append(root.data)
            elements += self.in_order_traversal(root.right)

        return elements

    def is_same_tree(self, p, q):

        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.data != q.data:
            return False
        else:
            return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)


tree2 = BinaryTreeNode(3)
tree2.left = BinaryTreeNode(9)
tree2.right = BinaryTreeNode(20)
tree2.right.left = BinaryTreeNode(15)
tree2.right.right = BinaryTreeNode(7)

tree = BinaryTreeNode(3)
tree.left = BinaryTreeNode(9)
tree.right = BinaryTreeNode(20)
tree.right.left = BinaryTreeNode(15)
tree.right.right = BinaryTreeNode(7)


print(tree2.in_order_traversal(tree2))
print(tree.is_same_tree(tree, tree2))

