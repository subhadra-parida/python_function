### Factorial Number in function.....
def fun(a):
	fact=1
	while a>0:
		fact=fact*a
		a=a-1
		print(fact,"factorial number")
a=int(input("enter any number="))
fun(a)