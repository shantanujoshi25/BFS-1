# // Time Complexity : O(n) 
# // Space Complexity : O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:  
            return []
        result = []


        def lot(node,level):
            if(node is None):
                return 

            if(len(result)<=level):
                result.append([node.val])
            else:
                result[level].append(node.val)
            
            lot(node.left,level+1)
            lot(node.right,level+1)
        
        lot(root,0)
        return (result)
        