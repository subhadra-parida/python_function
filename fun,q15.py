###How to define sum of avrrage number in function...
def function(a,b,c):
	i=0
	sum=0
	ave=0
	while i<3:
		num=int(input("enyer any number="))
		sum=sum+num
		print(sum)
		i=i+1
		ave=sum/3
	print(ave)
function(3,4,5)