# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []

        ans = []

        q = deque()
        q.append(root)

        while len(q) > 0 :

            sz = len(q)

            curLevel = []

            for _ in range(sz):
            
                cur = q.popleft()
                curLevel.append(cur.val)
 
                if cur.left != None:
                    q.append(cur.left)

                if cur.right != None:
                    q.append(cur.right)

            ans.append(curLevel)
        return ans[::-1]