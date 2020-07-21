#iterative method -- 

def binarysearch(arr,x,l,h):
    while l <= h:
        mid = (l + h)// 2 
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            h = mid -1 
        else:
            l = mid +  1
    return -1 
    
    
#recusive methods 
def binarysearch(arr,x,l,h):
    mid = (l+h)//2
    if l > h:
        return False
    elif x == arr[mid]:
        return mid 
    elif x > arr[mid]:
        return binarysearch(arr,x,mid+1,h)
    else:
        return binarysearch(arr,x,l,mid-1)
    
    
    

ls = [1,2,3,4,5,6,7,8,9]
# # x = 4
# # l = 2
# # h = 9  
print(binarysearch(ls,6,0,8))
