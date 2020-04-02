def largestalgo(lists):
    mixl = lists[0]
    max2 = None
    max3 = None
    for i in range(len(lists)):
        if lists[i] > mixl :
            mixl = lists[i]
        elif max2 == None or max2 < lists[i]:
            max2 = lists[i]
        elif max3 == None or max3 < lists[i] :
            max3 = lists[i]
    return mixl,max2,max3

            


def largestsort(lists):
    lists.sort(reverse= True)
    return lists[1]

def largestsorted(lists):
    lists = sorted(lists,reverse=True)
    return lists[1]



print(largestalgo([1,87,54,3,2,5,9,2,1]))
print(largestsort([1,87,54,3,2,5,9,2,1]))
print(largestsorted([1,87,54,3,2,5,9,2,1]))



