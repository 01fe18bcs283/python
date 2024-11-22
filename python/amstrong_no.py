def amstrong(n):
    
    digits=str(n)
    l=len(digits)
    r=0
    for i in digits:
        r += int(i)**l
    return n==r

n=int(input("enter the number:"))
if amstrong(n):
    print("it is a amstrong number")
else:
    print("it is not a amstrong number")
