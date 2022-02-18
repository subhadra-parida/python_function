# user is vvalid or not.......
def fun():
    a=input("Enter any paranthesis=")
    i=0
    while i<len(a):
        if a=="()":
            print("Valid")
        elif a=="(())":
            print("Valid")
        else:
            print("Invalid")
    i=i+1
fun()