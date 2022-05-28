# hashmap dictionary with array
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def connectHelper(node, level, idx_map_array):
            if not node:
                return
            
            if not level in idx_map_array:
                idx_map_array[level] = []
                
            idx_map_array[level].append(node)
            
            level = level + 1
            connectHelper(node.left, level, idx_map_array)
            connectHelper(node.right, level, idx_map_array)
            
            return
        
        
        if not root:
            return root
        
        # use hashmap array 
        idx_map_array = {}
        level = 0
        
        connectHelper(root, level, idx_map_array)
        
        # link map array
        for level in idx_map_array:
            for count,node in enumerate(idx_map_array[level]):
                #print("array fun  - " + str(idx_map_array[level]))
                if count+1 == len(idx_map_array[level]):
                    node.next = None
                else:
                    #print("count+1  - " + str(count+1))
                    node.next = idx_map_array[level][count+1]
        return root

