
#factorial of no without recusion 
n =5
fact = 1 
for i in range(1,n+1):
    fact = fact * i

print(fact)

#factorial of no. with recursion


def fact(n):
    if n == 1:
        return n
    else :
        return n * fact(n-1)

print(fact(5))
    
    
    

    




#find the nth term of fibnnaco series 

nth = int(input("rnyrt the nth term"))

n1 , n2 = 0, 1
count = 0

if nth < 1 :
    print("this is not a valid no")
elif  nth == 1:
    print(n1)
else:
    while count < nth:
        print(n1)
        nh = n1 + n2
        # update values
        n1 = n2
        n2 = nh
        count += 1



#no. is prime or not 

import math

def check(n):
    if n >1:
        for i in range(2,n):
            if (n%i) == 0:
                flag = 0
                break
        else:
            flag = 1
    else:
        flag = 0
                
    if flag == 0:
        print("not prime")
    else:
        print("prime")
        
        
check(3)


# largest of 3 numbers 
        
print(largest(21,5,7))

def calsqrt(a,b,c):
    d = 5
    D = b**2 - 4 * a * c
    if D >= 0:
        r1 = -(b) +  math.sqrt(D) / 2*a
        r2 = -(b) - math.sqrt(D) / 2*a 
        return r1,r2,d
        
    else:
        rp = b/2*a
        ip = math.sqrt(-D)/2*a
        return rp , ip,d
        

    
