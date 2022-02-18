def fun(*a):
    i=0
    while i<len(a):
        j=0
        while j<len(a):
            k=0
            while k<len(a):
                print(a[i]+a[j]+a[k])
            k=k+1
        j=j+1
    i=i+1
fun(12,23,34,45)
            