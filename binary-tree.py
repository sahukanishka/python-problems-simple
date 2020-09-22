class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right =None
        
class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)
        
    def printtree(self,traversal_type):
        if traversal_type == "preorder":
            return self.preorder(self.root,"")
        else:
            return -1
        
    def preorder(self,start,traversal):
        if start:
            traversal += (str(start.value)) + "-"
            traversal = self.preorder(start.left,traversal)
            traversal = self.preorder(start.right,traversal)
        return traversal 
        
    def sizeoftree(self):
        if self.root == None:
            return 0
        stak = []
        size = 1
        stak.append(self.root)
        while stak:
            node = stak.pop()
            if node.left:
                size +=1
                stak.append(node.left)
            if node.right:
                size+=1
                stak.append(node.right)
                
        return size
        
    def size_(self,node):
        if node is None:
            return 0
        return 1 + self.size_(node.left) + self.size_(node.right)
        
        
  
  
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right= Node(3)
tree.root.left.left= Node(4)
tree.root.left.right= Node(5)
tree.root.right.left= Node(9)
tree.root.right.right= Node(10)
tree.root.left.left.left= Node(6)
tree.root.left.left.right= Node(7)
tree.printtree("preorder")
print(tree.sizeoftree())
print(tree.size_(tree.root))
