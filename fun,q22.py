#Numbers are divisible by 3 print'nav', by 7 print'Gurukul', by both 'NavGurukul'....
def func(num):
	i=1
	while i<=num:
		if i%3==0:
			print('Nav')
		elif i%7==0:
			print('Gurukul')
		elif i%3==0 and i%7==0:
			print('NavGurukul')
		else:
			print(i)
		i=i+1
num=int(input('enter any number'))
func(num)