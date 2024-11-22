def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def product(x,y):
    return x*y

def div(x,y):
    return x/y

def even(x):
    if(x%2==0):
        return True
    else:
        return False
    
def prime(n):
    if n <=1:
        return False
    for i in range(2,int(n/2)+1):
        if n%2==0:
            return False
    return True

def amstrong(n):
    
    digits=str(n)
    l=len(digits)
    r=0
    for i in digits:
        r += int(i)**l
    return n==r

def reverse(l):

    new_list=l[::-1]
    return new_list
    

import math
def factorial(n):
    r=1
    for i in range(2,n+1):
        r *= i

    return r

def factors(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    return l

def count_factor(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count += 1
    return count


