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



def matching(ele,top):
    if ele == ")" and top == "(":
        return True 
    elif ele == "]" and top == "[":
        return True
        
    elif ele == "}" and top == "{":
        return True 
    else:
        return False


def check_bal(strings):
    stk = Stack()
    index = 0
    balanced = True 
    
    while index < len(strings) and balanced:
        ele = strings[index]
        if ele in "({[":
            stk.push(ele)
            print("*")
            
        else:
            if stk.is_empty():
                balanced = False
                print("**")
            else:
                top = stk.pop()
                if not matching(ele,top):
                    balanced = False
                    print("***")
        index += 1
        
        
    if stk.is_empty() and matching:
        return True 
    else:
        return False 
        
s = "({})"        
print(check_bal(s))
                
