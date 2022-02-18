# Aapko sort function ka use kr ke di hue list ko sort krna hai.
unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
def fun():
    i=0
    while i<len(unorder_list):
        a=i
        j=i+1
        while j<len(unorder_list):
            if unorder_list[a]>unorder_list[j]:
                a=j
            j=j+1
        unorder_list[i],unorder_list[a]=unorder_list[a],unorder_list[i]
        i=i+1
    print(unorder_list)
fun()