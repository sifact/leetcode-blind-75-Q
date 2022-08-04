class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    #                     03
    #                     /\
    #                    9 20
    #                      /\
    #                    15  7

    # preorder = [3, 9, 20, 15, 7]  start with tree root
    # inorder = [9, 3, 15, 20, 7]   tree root stay in between of left tree and right tree
    root = BinaryTreeNode(preorder[0])
    mid = inorder.index(preorder[0])

    root.left = build_tree(preorder[1:mid + 1], inorder[:mid])
    root.right = build_tree(preorder[mid + 1:], inorder[mid + 1:])

    return root


def inorder_traversal(root):
    elements = []

    if root.left:
        elements += inorder_traversal(root.left)

    elements.append(root.val)

    if root.right:
        elements += inorder_traversal(root.right)

    return elements


pre_order = [3, 9, 20, 15, 7]
in_order = [9, 3, 15, 20, 7]
tree = build_tree(pre_order, in_order)
print(inorder_traversal(tree))

