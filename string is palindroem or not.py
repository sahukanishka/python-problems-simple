#the mean of string is palindrome or not is to check the srting is same charecter as from left and from right.
#so we have to match the elemnt of the string 
#first method
#lets create a function to chcek 
def palindrome(s):
# this function is passing with the argument string to check 
    l = len(s) 
    for i in range(l):
        if s[i] != s[l-1-i]:
            return 'not palindrome'
        else:
            pass
    return 'palindrome'

print(palindrome('aaccc'))

#second method 
#in this method we are going to use reverse buildin function to reverse the string and stroe in the variable 
#if the original string is equle to the reverse string 
#if yes string is palindrome 
def revpalaindrome(s):
    r = "".join(reversed(s))
    print(r)
    for i in range(len(s)):
        if s[i] == r[i]:
            pass
        else:
            return False
    return True 

s = 'aaasas'
ans = revpalaindrome(s)
if (ans):
    print('yes')
else:
    print('no')
            
#or be can directly compare the reverse string with given string 
#third method

def comstring(s):
    r = "".join(reversed(s))
    if r == s:
        return "yes"
    else:
        return "no"

print(comstring("aaabbcbbaaa"))

