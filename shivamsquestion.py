# def mapnew(lst):
#     count = 0
#     clist = []
#     for i in lst:
#         count = count+1 
#         nlist = lst[count]
#         clist.append(nlist)
#         if count == len(lst):
#             break
#     return clist

# def mapnew(lst):
#     clist = []
#     for i in lst:
#         if i%2 == 0:
#             i=i**2
#             clist.append(i)
#         else:
#             pass
#     return clist
# mapnew([1,2,3,4,5,6,7])


def mapnew(strr):
    count = 1
    clist = ''
    for x in strr:
        if count%2==0:
            x = int(x)
            x =x**2
            x = str(x)
            clist = clist + x
        count = count+1 
    return clist[:4]



print(mapnew('12345678'))