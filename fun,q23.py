#input ka use karke greatest value print karo. Without using loop....
def fun(n1,n2,n3):
	if n1> n2 and n1>n3:
		print(n1,"is gteater")
	elif n2>n1 and n2>n3:
		print(n2,"is greater")
	elif n3>n1 and n3>n2:
		print(n3,"is greater")
	else:
		print("not")
n1=int(input("enter any number="))
n2=int(input("enter any number="))
n3=int(input("enter any number="))
fun(n1,n2,n3)