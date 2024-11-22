def sum(n):
    t=0
    while n>0:
        t += n%10
        n //=10
    return t

n=int(input("enter the number:"))
print(f"sum of digits in number is:{sum(n)}")


def sum1(n1):
    t=0
    for i in str(n1):
        t+=n1%10
        n1//=10
    return t

n1= int(input("enter the number:"))
print(f"sum of digits in number are : {sum1(n1)}")

def sum3(n3):
    t=sum(map(int,str(n3)))
    return t

n3= int(input("enter the number"))
print(f"sum of digits are:{sum3(n3)}")