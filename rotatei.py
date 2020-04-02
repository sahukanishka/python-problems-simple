def rotatei():
    print('t')
    t = int(input())
    print('n')
    n = int(input())
 #len of string
    print('q')
    q = int(input())
 #num of query
    print('s')
    s = str(input())
    j = len(s)
    if j == n:
        print('yes')
        lst=[]
        for i in range(0,q):
            ele=[int(input()),int(input())]
            lst.append(ele)
    print("all query is taken")
    print(lst)
    for j in range(q):
        s = v
        k = lst[j][0]
        it = lst[j][1]
        s = s[-k] + s[:-k]
        print("after query")
        print(s[it])





print(rotatei())
