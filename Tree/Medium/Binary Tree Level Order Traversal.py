from collections import deque


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    """def level_order_traversal(self, root):
        elements = []

        d = deque([root])

        while d:
            node = d.popleft()
            if node:
                elements.append(node.data)
                d.append(node.left)
                d.append(node.right)
        return elements"""

    def level_order_traversal(self, root):
        res, d = [], deque([(root, 0)])

        while d:
            node, level = d.popleft()

            if node:
                if len(res) < level + 1:
                    res.append([])

                res[level].append(node.data)
                d.append((node.left, level + 1))
                d.append((node.right, level + 1))
        return res


#                  04
#                  /\
#                 2  7
#                /\  /\
#               1 3 6  9


tree = BinaryTreeNode(4)
tree.left = BinaryTreeNode(2)
tree.left.left = BinaryTreeNode(1)
tree.left.right = BinaryTreeNode(3)

tree.right = BinaryTreeNode(7)
tree.right.left = BinaryTreeNode(6)
tree.right.right = BinaryTreeNode(9)

print(tree.level_order_traversal(tree))
