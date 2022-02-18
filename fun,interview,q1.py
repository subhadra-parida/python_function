# Using function print("1st & 3rd element).........
def fun():
    name=["Barsha","Lisa","Puja"]
    i=0
    list=[]
    while i<len(name):
        if name[i]==name[0]:
            pass
        else:
            list.append(name[i])
        i=i+1
    print(list)
fun()
