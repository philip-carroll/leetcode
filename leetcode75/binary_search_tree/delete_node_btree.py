from typing import Optional

from leetcode75.btree import TreeNode, deserialize


class Solution:
    def inorder_successor(self, node: TreeNode):

        ios = (TreeNode(float('inf')), None)

        visited = [(node, None)]
        first = True

        while visited:
            node, parent = visited.pop()

            if not first and node.val < ios[0].val:
                ios = (node, parent)

            if node.right:
                visited.append((node.right, node))

            if not first and node.left:  # inorder successor will always be to RHS of root at first level
                visited.append((node.left, node))

            if first:
                first = False

        return ios

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        del_root = False

        if root:
            if root.val == key:
                del_root = True
                if not root.right and not root.left:
                    return None

            visited = [(root, None)]

            while visited:
                node, parent = visited.pop()

                if node.val == key:
                    l = None
                    r = None

                    if not node.left and not node.right:  # leaf node
                        if parent.left == node:
                            parent.left = None
                        else:
                            parent.right = None

                    elif not node.left and node.right:  # only right child
                        node.val = node.right.val
                        if node.right.left:
                            l = node.right.left
                        if node.right.right:
                            r = node.right.right
                        node.left = l
                        node.right = r

                    elif node.left and not node.right:  # only left child
                        node.val = node.left.val
                        if node.left.left:
                            l = node.left.left
                        if node.left.right:
                            r = node.left.right
                        node.left = l
                        node.right = r

                    else:  # both children - find inorder successor
                        left_tmp = node.left
                        ios = self.inorder_successor(node)

                        if not ios[1].val == key:  # we're not removing the ios parent
                            if ios[1].left == ios[0]:  # ios one level below
                                ios[1].left = ios[0].right
                            else:
                                ios[1].right = None
                        else:  # we are removing the ios parent
                            if ios[1].left == ios[0]:  # ios one level below
                                left_tmp = None
                            else:
                                node.right = ios[0].right

                        node.val = ios[0].val
                        node.left = left_tmp

                    if del_root:
                        root = node

                    break
                else:
                    if node.right:
                        visited.append((node.right, node))

                    if node.left:
                        visited.append((node.left, node))

        return root


if __name__ == '__main__':
    sol = Solution()

    root = deserialize(
        # '[5,3,6,2,4,null,7]'
        '[2,0,33,null,1,25,40,null,null,11,31,34,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,35,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,null,null,38,null,41,null,null,null,47,49,null,null,5,null,13,15,21,23,null,28,37,null,null,null,null,null,null,null,null,8,null,null,null,17,19,null,null,null,null,null,null,null,7,null,16,null,null,20,6]'
    )

    key = 33

    res = sol.deleteNode(root, key)
    print(res)
