# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        visited = [(root, 1)]
        max_depth = 0

        while visited:
            node, depth = visited.pop()
            if depth > max_depth:
                max_depth = depth

            if node.right:
                visited.append((node.right, depth + 1))
            if node.left:
                visited.append((node.left, depth + 1))

        return max_depth


if __name__ == '__main__':
    sol = Solution()

    root = TreeNode(1, TreeNode(2, TreeNode(4), right=TreeNode(5)), TreeNode(3))
    print(sol.maxDepth(root))
    # root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    # print(sol.maxDepth(root))
    # root = TreeNode(1, TreeNode(2), TreeNode(3))
    # print(sol.maxDepth(root))
    # root = TreeNode(1, None, TreeNode(2))
    # print(sol.maxDepth(root))
    # root = TreeNode(1)
    # print(sol.maxDepth(root))
    # root = None
    # print(sol.maxDepth(root))
