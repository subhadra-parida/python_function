##How to define the sum of 10 which numbers are multiple by 3/5...
def limit():
	num=int(input("enter any number"))
	i=0
	sum=0
	while i<=num:
		if i%3==0 or i%5==0:
			sum=sum+i
		i=i+1
	print(sum)
limit()