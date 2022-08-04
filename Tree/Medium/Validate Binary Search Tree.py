def is_valid_bst(root):
    def valid(node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False

        return (valid(node.left, left, node.val) and
                valid(node.right, node.val, right))

    return valid(root, float('-inf'), float('inf'))


class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


tree = BinaryTreeNode(2)
tree.left = BinaryTreeNode(4)
tree.right = BinaryTreeNode(3)
print(is_valid_bst(tree))
