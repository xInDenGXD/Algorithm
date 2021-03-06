# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

## Node ##
class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = node
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
          
          
########################
# double linked list
#######################
## 
## each nodes tracks previous and next node
## list also tracks first and last node
##
class DNode:
    def __init__(self, data, previous_node, next_node):
        self.previous_node = previous_node
        self.next_node = next_node
        self.data = data
    
    def __str__(self):
        return_s = ""
        if self.previous_node:
            return_s = return_s +  " previous node - " + str(self.previous_node.data)
        if self.next_node:
            return_s = return_s + " next node - " + str(self.next_node.data)
        
        return return_s
        
class DoublylinkedList:
    def __init__(self, first_node, last_node):
        self.first_node = first_node
        self.last_node = last_node
    
    def insert_at_end(self, value):
        if self.last_node:
            last_node = self.last_node
            new_node = DNode(value, last_node, None)
            last_node.next_node = new_node
            self.last_node = new_node
        else:
            new_node = DNode(value, None, None)
            self.last_node = new_node
            self.first_node = new_node
            
    def remove_from_front(self)
        removed_node = self.first_node 
        self.first_node = self.first_node.next_node
        self.first_node.previous = None
        
class Queue:
    def __init__(self, value):
        new_node = DNode(value, None, None)
        self.queue = DoublylinkedList(new_node)
    
    #
    def enqueue(self, value):
        self.queue.insert_at_end(value)
        
    def read(self):
        if self.queue.first_node:
            return self.queue.first_node.data
        else:
            return None
            
    def dequeue(self):
        self.queue.remove_from_front
    
    
