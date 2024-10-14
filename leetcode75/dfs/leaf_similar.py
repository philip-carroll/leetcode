from typing import Optional

from leetcode75.btree import deserialize, TreeNode


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return get_leaf_seq(root1) == get_leaf_seq(root2)


def get_leaf_seq(root: TreeNode):
    leaf_seq = []
    visited = [root]

    while visited:
        node = visited.pop()

        if node.right:
            visited.append(node.right)
        if node.left:
            visited.append(node.left)
        if not (node.right or node.left):
            leaf_seq.append(node.val)

    return leaf_seq


if __name__ == '__main__':
    sol = Solution()

    # res = sol.leafSimilar(deserialize('[3,5,1,6,2,9,8,null,null,7,4]'),
    #                       deserialize('[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'))
    # print(res)
    res = sol.leafSimilar(deserialize('[1,2]'),
                          deserialize('[2,2]'))
    print(res)
