# Aapko sum function ka use krke di hue list ke element ka sum print krvana hai.
numbers=[1,2,3,4,5]
def func():
    i=0
    sum=0
    while i<len(numbers):
        sum=sum+numbers[i]
        i=i+1
    print(sum)
func()