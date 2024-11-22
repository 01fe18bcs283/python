s=input("entr the string:")
l=s.split()
l2=[]
i=0
while i<len(l):
    l2.append(l[i][::-1])
    i+=1
o=' '.join(l2)
print(o)