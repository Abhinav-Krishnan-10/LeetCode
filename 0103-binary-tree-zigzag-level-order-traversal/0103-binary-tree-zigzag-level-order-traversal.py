# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
            
        ans = []

        q = deque()
        q.append(root)

        lvl = 1
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

            if lvl % 2 == 0:
                curLevel.reverse()
            
            ans.append(curLevel)

            lvl += 1
        
        return ans