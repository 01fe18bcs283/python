def even(x):
    if x%2==0:
        return True
    else:
        return False
L=[2,3,4,5,6,7,8,9,10]
L1=list(filter(even,L))
print(L1)

#with lambda

L2=list(filter(lambda x:x%2==0,L))
print(L2)