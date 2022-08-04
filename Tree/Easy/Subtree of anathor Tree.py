class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def inorder_traversal(self, root):
        elements = []

        if root.left:
            elements += self.inorder_traversal(root.left)

        elements.append(root.val)

        if root.right:
            elements += self.inorder_traversal(root.right)

        return elements

    def is_sub_tree(self, s, t):
        if not (s and t):
            return True
        if not t:
            return True
        if not s:
            return False
        return self.is_same(s, t) or self.is_same(s.left, t) or self.is_same(s.right, t)

    def is_same(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val == t.val:
            return True
        return self.is_same(s.left, t.left) and self.is_same(s.right, t.right)


#                       03
#                       /\
#                      4  5
#                     /\
#                    1  2
tree = BinaryTreeNode(3)
tree.left = BinaryTreeNode(4)
tree.left.left = BinaryTreeNode(1)
tree.left.right = BinaryTreeNode(2)

tree.right = BinaryTreeNode(5)


#                     04
#                     /\
#                    1  2
tree2 = BinaryTreeNode(4)
tree2.left = BinaryTreeNode(1)
tree2.right = BinaryTreeNode(2)

print(tree.inorder_traversal(tree2))
print(tree.is_sub_tree(tree, tree2))



