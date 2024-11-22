tuple1 = ((2, 5), (2, 2), (2, 4), (2, 3), (2, 1))
tuple2=list(tuple1)
print(tuple2)
s=sorted(tuple2,key=lambda x :x[-1])
print(s)




t1 = ((2, 5), (2, 2), (2, 4), (2, 3), (2, 1))
n=len(t1)
fi=[]
sec=[]
for i in range(n):
    for j in range(0,2):
        if j==0:
            fi.append(t1[i][j])
        else:
            sec.append(t1[i][j])

t2=()
new_t=()
sec.sort()
for i in range (n):
    t2 = (fi[i],sec[i])
    new_t+=t2,

print(new_t)
