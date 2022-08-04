from collections import deque


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

    #  Recursion
    def invert_tree(self, root):
        if root:
            root.left, root.right = self.invert_tree(root.right), self.invert_tree(root.left)
        return root

    #  BFS
    def invert_tree2(self, root):
        d = deque([root])

        while d:
            node = d.popleft()
            if node:
                node.left, node.right = node.right, node.left
                d.append(node.left)
                d.append(node.right)
        return root


#                  04                                    04
#                  /\                 invert             /\
#                 2  7                ----->            7  2
#                /\  /\                                /\  /\
#               1 3 6  9                              9 6 3  1
tree = BinaryTreeNode(4)
tree.left = BinaryTreeNode(2)
tree.left.left = BinaryTreeNode(1)
tree.left.right = BinaryTreeNode(3)

tree.right = BinaryTreeNode(7)
tree.right.left = BinaryTreeNode(6)
tree.right.right = BinaryTreeNode(9)

print(tree.print_tree())
#  tree.invert_tree(tree)
tree.invert_tree2(tree)
print(tree.print_tree())
