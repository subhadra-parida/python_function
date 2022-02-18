# How to print sum in list.............
def fun():
    a=["a",1,0.4,"Shubha",3]
    i=0
    sum=0
    while i<len(a):
        if type(a[i])==int or type(a[i])==float:
            sum=sum+a[i]
        else:
            print(a[i])
        i=i+1
    print(sum)
fun()
