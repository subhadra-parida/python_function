# write a python program how to print maximum list in the main list.....
def fun():
    a=[[1,4],[3,2,6],[4,7,9,8,7,6],[6,1],[5,6,9,8]]
    i=0
    max=0
    min=0
    while i<len(a):
        if len(a[i])>min:
            min=len(a[i])
            max=a[i]
        i=i+1
    print(max)
fun()

