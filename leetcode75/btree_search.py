# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        visited = [root]

        while visited:
            node = visited.pop()

            if node.val == val:  # we've found the target val
                return node

            if node.right:
                visited.append(node.right)
            if node.left:
                visited.append(node.left)

        return None


if __name__ == '__main__':
    sol = Solution()

    root = TreeNode(4, TreeNode(2, TreeNode(1), right=TreeNode(3)), right=TreeNode(7))
    # root = TreeNode(4, TreeNode(2, TreeNode(1), right=TreeNode(3)), right=TreeNode(7))
    # root = TreeNode(4)
    val = 2

    print(sol.searchBST(root, val))
