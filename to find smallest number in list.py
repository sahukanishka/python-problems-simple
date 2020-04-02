import math
def smallnumalgo(lists):
    minl = lists[0]
    for i in range(len(lists)):
        if lists[i] < minl:
            minl = lists[i]
    return minl 



def smallnum(lists):
    m = min(lists)
    return m 


def smallnumsorted(lists):
    lists = sorted(lists)
    return lists[0]

def smallnumsort(lists):
    lists.sort()
    return lists[0]
#to run a function 

print(smallnumalgo([5,6,1,7,8,2,3,4,5,6,7]))  
print(smallnum([1,2,3,4,52,21,1]))
print(smallnumsorted([2,2,1,4,6,7,85,41,1]))
print(smallnumsort([2,2,1,4,6,7,85,41,1]))
