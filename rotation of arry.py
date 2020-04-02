#arr - arry to rotate
#d -  element 
#n - len of the arry 

def arryrotate(arr,d,n):
    l =arr[0:d]
    print(l)
    s = arr[d:] 
    print(s)
    return s+l

print(arryrotate([1,2,33,5,6,7],3,6))