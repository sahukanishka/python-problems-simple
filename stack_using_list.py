class Stack:
    def __init__(self):
        self.list = []
        
    def push(self,item):
        self.list.append(item)
    
    def pop(self):
        return self.list.pop()
    
    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False
            
    def peek(self):
        if not self.is_empty() :
            return self.list[-1]
        else:
            return False
            
    def items(self):
        return self.list 
        
   
    def count_len(self):
        return len(self.list)
        


stk = Stack()
stk.push('A')
stk.push('B')
stk.push('C')
stk.push('D')
print(stk.items())
stk.pop()
print(stk.items())
print(stk.peek())
print(stk.count_len())
print(stk.is_empty())
