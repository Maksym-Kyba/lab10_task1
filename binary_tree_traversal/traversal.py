# class Solution(object):
#     def hasPathSum(self, root, targetSum):
#         """
#         :type root: Optional[TreeNode]
#         :type targetSum: int
#         :rtype: bool
#         """
#         def recurse(node, local_sum):
#             if not (node.left or node.right):
#                 return local_sum + node.val == targetSum

#             res_left = res_right = False
#             if node.left is not None:
#                 res_left = recurse(node.left, local_sum + node.val)

#             if node.right is not None:
#                 res_right = recurse(node.right, local_sum + node.val)


#             return res_left or res_right

#         if root is None:
#             return False
#         return recurse(root, 0)

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def pre_order(node):
    order = []

    def recurse(node, order):
        if not (node.left or node.right):
            return order + [node.data]

        order = order + [node.data]

        if node.left is not None:
            order = recurse(node.left, order)

        if node.right is not None:
            order = recurse(node.right, order)

        return order

    if not node.left and not node.right:
        return order
    return recurse(node, order)


# In-order traversal
def in_order(node):
    order = []

    def recurse(node, order):
        if not (node.left or node.right):
            return order + [node.data]

        if node.left is not None:
            order = recurse(node.left, order)

        order = order + [node.data]

        if node.right is not None:
            order = recurse(node.right, order)

        return order

    if not node.left and not node.right:
        return order
    return recurse(node, order)

# Post-order traversal
def post_order(node):
    order = []

    def recurse(node, order):
        if not (node.left or node.right):
            return order + [node.data]

        if node.left is not None:
            order = recurse(node.left, order)

        if node.right is not None:
            order = recurse(node.right, order)

        order = order + [node.data]

        return order

    if not node.left and not node.right:
        return order
    return recurse(node, order)


leaf_7 = Node(7)
leaf_6 = Node(6)
leaf_5 = Node(5)
leaf_8 = Node(8)
leaf_9 = Node(9)
root_3 = Node(3, leaf_8, leaf_9)
root_4 = Node(4, leaf_6, leaf_7)
root_2 = Node(2, root_4, leaf_5)
root = Node(1, root_2, root_3)

print(post_order(root))
print(pre_order(root))
print(in_order(root))
