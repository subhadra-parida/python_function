#length question in function......
def function(str1,str2):
	if str1>str2:
		return str1
	elif str1==str2:
		return str1,str2
	else:
		return str2
str1=input("enter any name=")
str2=input("enter any name=")
length=function(str1,str2)
print(length)