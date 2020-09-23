class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
class Bst:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        if self.root is None:
            node = Node(value)
            self.root = node
        else:
            self._insert(value,self.root)
            
    def _insert(self,data,curr_node):
        if data < curr_node.data:
            if curr_node.left is None:
                node = Node(data)
                curr_node.left = node
            else:
                self._insert(data,curr_node.left)
            
        elif data > curr_node.data:
            if curr_node.right is None:
                node = Node(data)
                curr_node.right = node
            else:
                self._insert(data,curr_node.right)
                
        else:
            print("not inserted")
            
            
    def findele(self,value,root):
        if value == self.root.data:
            return True 
        elif value < self.root.data and self.root.left:
            return self.finele(value,self.root.left)
        elif value > self.root.data and self.root.right:
            return self.findele(value,self.root.right)
        else:
            return False 
            
    def inorder(self):
        if self.root :
            return self.inorder_print(self.root)
            
    def inorder_print(self,curr_node):
        if curr_node:
            self.inorder_print(curr_node.left)
            print(str(curr_node.data))
            self.inorder_print(curr_node.right)
        
            
            

tree = Bst()
tree.insert(5)
tree.insert(1)
tree.insert(7)
tree.insert(2)
tree.insert(9)
tree.insert(0.5)
tree.insert(4)

tree.inorder()



            
            
                
            
            
        
