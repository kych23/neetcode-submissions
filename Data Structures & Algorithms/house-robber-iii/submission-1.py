# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# MaxAmount[node] = MaxAmount[node] + 
# 
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
          return 0

        # returns [maxWithRoot, maxWithoutRoot]
        def dfs(root):

          # base case
          if not root:
            return [0,0]
          elif not root.left and not root.right:
            return [root.val, 0]

          left = dfs(root.left)
          right = dfs(root.right)
          maxWithRoot = root.val + left[1] + right[1]
          maxWithoutRoot = max(left) + max(right)
          return [maxWithRoot, maxWithoutRoot]
        
        return max(dfs(root))