def shownumber():
	num=int(input("enter any number"))
	i=0
	while i<=num:
		if i%2==0:
			print(i,"is even")
		else:
			print(i,"is odd")
		i=i+1
shownumber()