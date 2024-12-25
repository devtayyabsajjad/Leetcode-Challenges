from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestValues(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        max_value = float('-inf')  # Initialize to negative infinity for comparison

        for _ in range(level_size):
            node = queue.popleft()
            max_value = max(max_value, node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(max_value)

    return result

# Example usage:
# Building the binary tree [1, 3, 2, 5, 3, null, 9]
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

# Call the function
output = largestValues(root)
print(output)  # Output: [1, 3, 9]
