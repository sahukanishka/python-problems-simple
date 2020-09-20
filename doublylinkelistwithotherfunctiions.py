class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
            new_node.next = None
            new_node.prev = None
            return 
            
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            new_node = Node(data)
            itr.next = new_node
            new_node.prev = itr
            new_node.next = None
            return 
            
    
    def prepend(self,data):
        if self.head == None:
            self.append(data)
            return 
        else:
            itr = self.head
            new_node = Node(data)
            new_node.next = itr
            itr.prev = new_node
            new_node.prev = None
            self.head = new_node
            return
    def printnode(self):
        itr = self.head
        ans = ""
        while itr:
            ans+= str(itr.data) + "-->"
            itr= itr.next  
        return ans 
            
    
    def delete(self,data):
        itr = self.head
        while itr:
            if itr.data == data:
                if itr.next == None and itr.prev ==None:
                    itr = None
                    return 
                elif itr.next == None and itr.prev != None:
                    current = itr.prev
                    itr.prev = None 
                    current.next = None 
                    return 
                elif itr.prev == None and itr.next != None:
                    current = itr.next
                    itr.next = None 
                    current.prev = None
                    self.head = current
                    return 
                else:
                    nxt = itr.next
                    prv = itr.prev
                    prv.next = nxt
                    nxt.prev = prv
                    itr.next = None
                    itr.prev = None 
                    return 
                    
            itr = itr.next
            
    def reverse(self):
        temp =None
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.next
            
        if temp is not None:
            self.head = None
            
    def removedupli(self):
        itr = self.head
        seen = {}
        while itr:
            x = itr.data
            if x not in seen:
                seen[x] = True 
            else:
                self.delete(x)
            itr = itr.next
            
            
        
                    
                    
                
    
n = Linkedlist()
n.append(1)
n.append(2)
n.prepend(5)
n.append(3)
n.append(4)
n.prepend(5)
n.delete(1)
n.append(6)
n.append(6)

# print(n.printnode())
# n.reverse()
print(n.printnode())
n.removedupli()
print(n.printnode())

    
