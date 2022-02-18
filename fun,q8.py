#Aapko min function ka use karke di hue list me se sabse chhoto / minimum value print karvana hai....
list=[8,6,4,6,5,2]
def fun():
	i=0
	min=0
	while i<len(list):
		if min>list[i]:
			min=list[i]
		i=i+1
	print(min)
fun()