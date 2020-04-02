def findnlargestalgo(lists,n):
    final_list =[]
    for i in range(0,n):
        max1=0

        for j in range(len(lists)):
            if lists[j] > max1:
                max1 = lists[j];

        lists.remove(max1);
        final_list.append(max1)
    return final_list

def findnlargestsort(lists,n):
    lists.sort(reverse=True)
    return lists[0:n]

def findnlargestsorted(lists,n):
    lists = sorted(lists,reverse=True)
    return lists[0:n]


print(findnlargestsort([2,3,1,45,6,654,66,3],3))
print(findnlargestsorted([2,3,1,45,6,654,66,3],3))
print(findnlargestalgo([2,3,1,45,6,654,66,3],3))