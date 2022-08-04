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


def is_same_tree(p, q):

    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.data != q.data:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


#      01
#      /\
#     2  3
tree2 = BinaryTreeNode(3)
tree2.left = BinaryTreeNode(9)
tree2.right = BinaryTreeNode(20)
tree2.right.left = BinaryTreeNode(15)
tree2.right.right = BinaryTreeNode(7)

tree = BinaryTreeNode(20)
tree.left = BinaryTreeNode(9)
tree.right = BinaryTreeNode(3)
tree.right.left = BinaryTreeNode(15)
tree.right.right = BinaryTreeNode(7)

print(tree.print_tree())
print(is_same_tree(tree, tree2))
