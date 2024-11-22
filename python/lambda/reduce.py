from functools import reduce
def f1(x,y):
    return x+y
L=[10,20,30,40,50,60,70]
result=reduce(f1,L)
print(result)

#with lambda

result=reduce(lambda x,y: x if x > y else y,L)
print(result)


