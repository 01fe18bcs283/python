
def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True

def prime_all(l):
    l2=[]
    for i in l:
        if prime(i):
            l2.append(i)
    return l2

def max_prime(prime_list):
    max=prime_list[0]
    for i in prime_list:
        if i>max:
            max=i
    return max


l=[5,9,7,13,2,97,99]
prime_list=prime_all(l)
max_prime_number=max_prime(prime_list)
print(prime_list)
print("max number in prime list is:",max_prime_number)
