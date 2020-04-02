s="{()}("
def checkBrackets(s:str)->int:
    stack=[]
    brac={
        '(':')',
        '{':'}',
        '[':']'
    }
    for i in range(len(s)):
        if s[i] in "[({":
            print("push",s[i])
            
            stack.append(s[i])
            print(stack)
        elif len(stack)==0:
            return i+1
        elif s[i]==brac[stack[len(stack)-1]]:
            print("pop",s[i])
            stack.pop()
        else:
            print(i+1)
            return i+1
    print("outside")
    if stack==[]:
        return -1
    else:
        return len(s)+1
print(checkBrackets(s))