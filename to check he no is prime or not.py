n  = input("enter the no to check it is prime or not ")
n = int(n)
for i in range(2,n):
    if n%i == 0 :
        print("no is not prime")
        break
else:
    print("no is prime")