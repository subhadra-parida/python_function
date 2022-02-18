#How to print unlimit perfect number in function.....
def perfect(n):
	i=1
	while i<=n:
		j=1
		sum=0
		while j<i:
			if i%j==0:
				sum+=j
			j+=1
		if sum==i:
			print(i,"is a perfect number")
		else:
			print(i,"is not a perfect number")
		i+=1
num=int(input("enter any number"))
perfect(num)
