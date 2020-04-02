def findprime(i,j):
    for val in range(i,j+1):
        if val>1:
            for n in range(2,val):
                if (val%n)==0:
                    break
        else:
            print(val) 
   
   
   
findprime(11,25)