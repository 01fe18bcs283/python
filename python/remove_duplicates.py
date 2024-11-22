s=input("enter the string:")
l=[]
for i in s:
    if i not in l:
        l.append(i)
o=' '.join(l)
print(o)