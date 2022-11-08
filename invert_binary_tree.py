# simply recursively swap
# left = right and right = left
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            return TreeNode(root.val,
                            self.invertTree(root.right),
                            self.invertTree(root.left))
