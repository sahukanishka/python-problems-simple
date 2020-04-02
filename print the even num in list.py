def printeven(lists):
    for i in lists:
        if i%2==0:
            print(i)

def printevenwhile(lists):
    num = 0
    while(num<len(lists)):
        if num % 2==0:
def printodd(lists):
    for i in lists:
        if i%2!=0:
            print(i)


print(printeven([2,4,5,72,5,2,8,4]))
print(printodd([2,4,5,72,5,2,8,4]))