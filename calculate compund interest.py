def compoundint(ammount , rate , time ):
    return ammount *(pow((1+rate/100),time))

#testcase
print(compoundint(5000,5,1))