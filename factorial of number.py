def rot():
    s = input('enter the string ')
    a=  s[0]
    b = s[-1]
    c = s[1:-1]
    return b+c+a


print(rot())