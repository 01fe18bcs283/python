n=input("enter the string:")
d={}
for i in n:
    if i in d.keys():
        d[i] +=1
    else:
        d[i] =1
for k,v in d.items():
    
    print(f"{k}={v}times")
