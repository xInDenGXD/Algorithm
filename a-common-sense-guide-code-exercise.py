######################
### Chapter 14 - 1 ###
######################
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
## Node ##
class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node
    def __str__(self):
        if self.next_node:
            return f"data is {self.data} and next_node is {self.next_node}"
        else:
            return f"data is {self.data} and next_node is None"
            
## linked list ##
## read a 
class LinkList:
    def __init__(self, node):
        self.first_node = node
    
    def read(self, index):
        current_node = self.first_node
        current_index = 0
        while current_index < index:
            if current_node.next_node:
                current_node = current_node.next_node
            else:
                return None # cannot find the index
        return current_node.data # return node data
        
    # search
    def index_of(self, value):
        current_node = self.first_node
        current_index = 0
        while current_node.data != value:
            if current_node.next_node:
                current_node = current_node.next_node
            else:
                return None # cannot find node contains value 
        
        return current_node.index # return index of the node
    
    # insert
    def insert_at_index(self, index, value):
        
        if index == 0:
            new_node = Node(value,self.first_node)
            self.first_node = new_node
            return
        
        current_node = self.first_node
        current_index = 0
        
        while current_index < index-1:
            if current_node.next_node:
                current_node = current_node.next_node
            else:
                return None
         
        # current index-1
        if current_node.next_node:
            new_node = Node(value, current_node.next_node)
            current_node.next_node = new_node  
        else:
            return None
            
        return "insertion success"
    # deletion
    def delete_at_index(self,index):
        
        if index == 0:
            self.first_node = self.first_node.next_node
            return
        
        current_node = self.first_node
        current_index =0
        
        while current_index < index-1:
            if current_node.next_node:
                current_node = current_node.next_node
            else:
                return None
        # at index-1
        current_node.next_node = current_node.next_node.next_node
        return "deletion success"
       
    def print_all_node(self):
        if not self.first_node: # empty node situation
            return -1
          
        current_node = self.first_node
        while current_node:
            print(str(current_node.data))
            current_node = current_node.next_node
##############
# MAIN #######
##############
node_d = Node(3,None)
node_c = Node(6,node_d)
node_b = Node(2,node_c)
node_a = Node(8,node_b)

l = LinkList(node_a)
l.print_all_node()

m = LinkList(None)
m.print_all_node()

######################
### Chapter 14 - 2 ###
######################


