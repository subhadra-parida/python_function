number=[12,54,98,90,87,65]
def name():
    i=0
    max=0
    max2=0
    while i<len(number):
        if number[i]>max:
            max=number[i]
            max2=max
        if max2<number[i]<max:
            max2=number<[i]
        i+=1
    print(max)
name()