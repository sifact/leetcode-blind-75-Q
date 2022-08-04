# from collections import deque


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def max_path_sum(self, root):
        max_path = float("-inf")

        def get_max_gain(node):
            nonlocal max_path
            if node is None:
                return 0

            gain_on_left = max(get_max_gain(node.left), 0)
            gain_on_right = max(get_max_gain(node.right), 0)

            current_max_path = node.data + gain_on_left + gain_on_right
            max_path = max(max_path, current_max_path)

            return node.data + max(gain_on_right, gain_on_left)

        get_max_gain(root)
        return max_path

    def max_path_sum2(self, root):
        res = [root.data]

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0

            left_max = dfs(root.left)
            right_max = dfs(root.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # compute max path sum with split
            res[0] = max(res[0], root.data + left_max + right_max)

            return root.data + max(left_max, right_max)

        dfs(root)
        return res[0]


#                      -10
#                       /\
#                     9   20
#                         /\
#                       15  7
tree = BinaryTreeNode(-10)
tree.left = BinaryTreeNode(9)
tree.right = BinaryTreeNode(20)
tree.right.left = BinaryTreeNode(15)
tree.right.right = BinaryTreeNode(7)
print(tree.max_path_sum2(tree))
