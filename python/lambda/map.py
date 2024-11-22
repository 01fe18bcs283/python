def dbl(x):
    return 2*x
L=[2,3,4,5,6,7,8,9,10]
L1=list(map(dbl,L))
print(L1)


#with lambda
L2=list(map( lambda x:2*x, L))
print(L2)