def squre():
    l = input("enter the lenght of the squre :")
    l = int(l)
    return l*l 
def cicrle():
    r = input("enter the radious of the circle :")
    r = int(r)
    return 3.14*r**2
def rectangle():
    l = input("enter the lenght of the rectangle :")
    w = input("enter the weidth of the rectangle :")
    h = input("enter the height of the rectangle :")
    l = int(l)
    w = int(w)
    h = int(h)
    return l*w*h
def triangle():
    b = input("enter the base of the squre :")
    h = input("enter the height of the squre :")
    b = int(b)
    h = int(h)
    return b*h/2 
def findarea():
    f = input("which are you want to find :")
    if f == "squre":
        print(squre())
    elif f == "circle":
        print(cicrle())
    elif f == "rectangle":
        print(rectangle())
    elif f == "triangle":
        print(triangle())
    else:
        print("invalid input ")


findarea()
