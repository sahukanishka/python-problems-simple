def findarmstrong(n):
    orig = n 
    sum = 0 
    while n > 0 :
        sum  = sum + (n%10)*(n%10)*(n%10)
        n = n//10
    if orig == sum :
        print(orig ,": is armstrong")
    else:
        print(orig,":is not armstrong")


print(findarmstrong(153))