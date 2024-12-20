
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        def dfs(left, right, level):
            # Base case: If either left or right is None, stop recursion
            if not left or not right:
                return

            # If the current level is odd, swap the values
            if level % 2 == 1:
                left.val, right.val = right.val, left.val

            # Recursively call for the next level
            dfs(left.left, right.right, level + 1)
            dfs(left.right, right.left, level + 1)

        # Start DFS from level 1 with the children of the root
        dfs(root.left, root.right, 1)

        return root
