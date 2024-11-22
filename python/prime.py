def prime(n):
    if n <=1:
        return False
    for i in range(2,int(n/2)+1):
        if n%2==0:
            return False
    return True

n= int(input("enter the number:"))
if prime(n):
    print("its a prime number")
else:
    print("it is not a prime number")