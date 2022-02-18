def my_function(speed):
    point=(speed-70)//5*1
    if speed<=70:
        print("ok")
    if speed>70:
        print((speed-70)//5*1)
    if point>12:
        print("licence suspended")
speed=int(input("enter your speed  "))
my_function(speed)    