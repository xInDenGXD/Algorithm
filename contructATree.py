# LEET 106 
#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
                
        for i in range(len(postorder)):
            #print("setup hashmap - " + str([i]) + " VS " + str(postorder[i]))
            hashmap[postorder[i]] = i
                
        root       = TreeNode()
        root.val   = postorder[-1]
        index      = inorder.index(postorder[-1]) # subtree
        
        root.left  = self.buildSubTree(inorder[0:index], hashmap)
        root.right = self.buildSubTree(inorder[(index+1):len(inorder)], hashmap)
        
        return root
        
    def buildSubTree(self, inorder, hashmap):
       
        if len(inorder) == 0:
            #print("empty list")
            return None
        
        node = TreeNode()
        if len(inorder) == 1:
            node.val = inorder[0]
            #print("last node in the inorder - simply return - " + str(inorder) )
            return node
        
        #print("postorder is a list - check inorder - " + str(inorder) )
        #print("postorder is a list - check postorder - " + str(postorder) )    
        
        # find the subTreeRoot - highest index for postTree
        r_val   = 0
        p_index = 0
        i_index = 0
        r_index = 0
        for i in range(len(inorder)):
            p_index = hashmap[inorder[i]]
            if p_index > i_index:
                i_index = p_index
                r_index = i
                r_val   = inorder[i]
        
        node.val   = r_val    
       # print("node val set to " + str(node.val))
        
       # print("node index " + str(r_index) + " VS len:" + str(len(inorder)))
        
       # print("passing inorder left - " + str(inorder[0:r_index]))
        node.left  = self.buildSubTree(inorder[0:r_index], hashmap)
        
       # print("passing inorder right - " + str(inorder[r_index+1:len(inorder)]))
        node.right = self.buildSubTree(inorder[(r_index+1):len(inorder)], hashmap)
    
        return node
    
