def largestalgo(lists):
    mixl = lists[0]
    for i in range(len(lists)):
        if lists[i] > mixl:
            mixl = lists[i]
    return mixl
def largestsort(lists):
    lists.sort(reverse= True)
    return lists[0]

def largestsorted(lists):
    lists = sorted(lists,reverse=True)
    return lists[0]

def largestmax(lists):
    a = max(lists)
    return a 


print(largestalgo([1,87,54,3,2,5,9,2,1]))
print(largestmax([1,87,54,3,2,5,9,2,1]))
print(largestsort([1,87,54,3,2,5,9,2,1]))
print(largestsorted([1,87,54,3,2,5,9,2,1]))