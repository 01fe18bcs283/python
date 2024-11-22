def amstrong(start, end):
    l=[]
    for n in range(start,end+1):
        m=0
        num_str=str(n)
        digit=len(num_str)
        # m=sum(int(i)**digit for i in num_str)
        for i in num_str:
            m+=int(i)**digit

        if m==n:
            l.append(n)
    return l

start=int(input("enter the start range"))
end=int(input("enter the end range"))
a=amstrong(start,end)
print(f"amstrong numbers in range are:{a}")



    