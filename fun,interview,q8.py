# Write a program add the last list.....

a=[[1,4],[3,2,6],[9,8]]
i=0
m=[]
while i<len(a[i]):
    j=1
    while j<len(a[i]):
        if a[i]>a[j]:
            m.append(a[i])
        else:
            m.append(a[i])
        j=j+1
    i=i+1
print(m)
