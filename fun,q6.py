#Reverse function ka use kr ke aapko di hue list ka revrse print krna hai.
reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
def func():
    a=[]
    i=-1
    while i>=-len(reverse_list):
        a.append(reverse_list[i])
        i=i-1
    print(a)
func()