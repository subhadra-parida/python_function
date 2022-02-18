# Using indexing how to print(Lisa)...
def fun():
    a=["i","b","a","h"]
    b=a[0]
    a[0]=a[2]
    a[2]=a[3]
    a[3]=b[0]
    print(a)
fun()
