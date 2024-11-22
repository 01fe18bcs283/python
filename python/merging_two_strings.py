s1=input("enter first strings:")
s2=input("enter second string:")
merge=''
i,j=0,0
while i<len(s1) or j <len(s2):
    if i<len(s1):
        merge += s1[i]
        i += 1
    if j<len(s2):
        merge += s2[j]
        j += 1

print(merge)