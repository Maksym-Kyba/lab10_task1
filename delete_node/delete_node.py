# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def deleteNode(root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        def recurse(root, key):
            if root is None:
                return None

            if root.val == key:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left

                replace_node = root.right
                while replace_node.left:
                    replace_node = replace_node.left

                replace_node.left = root.left

                return root.right

            if key > root.val:
                root.right = recurse(root.right, key)
            else:
                root.left = recurse(root.left, key)

            return root

        recurse(root, key)
        return root

def deleteNode(root, key):
    """
    :type root: Optional[TreeNode]
    :type key: int
    :rtype: Optional[TreeNode]
    """
    def recurse(root, key):
        if root is None:
            return None

        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            replace_node = root.right
            while replace_node.left:
                replace_node = replace_node.left

            replace_node.left = root.left

            return root.right

        if key > root.val:
            root.right = recurse(root.right, key)
        else:
            root.left = recurse(root.left, key)

        return root

    recurse(root, key)
    return root

leaf_2 = TreeNode(2)
leaf_4 = TreeNode(4)
leaf_7 = TreeNode(7)
root_3 = TreeNode(3, leaf_2, leaf_4)
root_6 = TreeNode(6, None, leaf_7)
root = TreeNode(5, root_3, root_6)

x = deleteNode(root, 3)
print(x.val)
print(x.left.val)
print(x.left.left.val)
print(x.left.right)
print(x.right.val)
print(x.right.right.val)
