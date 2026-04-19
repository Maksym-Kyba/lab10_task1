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
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    sorted_trees = []

    def height(node):
        if not (node.left or node.right):
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        return max(left_height, right_height) + 1

    tree_height = height(node) + 1
    levels = {x: [] for x in range(tree_height)}

    def recurse(node, current_level):
        if not (node.left or node.right):
            levels[current_level].append(node.value)
            return None

        levels[current_level].append(node.value)

        if node.left:
            recurse(node.left, current_level + 1)
        if node.right:
            recurse(node.right, current_level + 1)

    recurse(node, 0)

    for value in levels.values():
        sorted_trees.extend(value)

    return sorted_trees


leaf_7 = Node(None, None, 7)
leaf_6 = Node(None, None, 6)
leaf_5 = Node(None, None, 5)
leaf_8 = Node(None, None, 8)
leaf_9 = Node(None, None, 9)
root_3 = Node(leaf_8, leaf_9, 3)
root_4 = Node(leaf_6, leaf_7, 4)
root_2 = Node(root_4, leaf_5, 2)
root = Node(root_2, root_3, 1)

print(tree_by_levels(root))
