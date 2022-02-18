# Print the last element is comes to 1st element & last is comes to 1st.....
def fun():
    list=[12,23,34,45,24]
    i=0
    while i<len(list):
        a=list[4],list[1],list[2],list[3],list[0]
        i=i+1
    print(a)
fun()


# OUTPUT........(24,23,34,45,12)