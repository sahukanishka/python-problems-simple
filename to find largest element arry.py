def greatelement(d,n):
    max = d[0]
    for i in range(1,n):
        if d[i] > max :
            max = d[i]
    return max 

# def greatelement(d):
#     return max(d)

print(greatelement([1,2,8,4,5,6],6))