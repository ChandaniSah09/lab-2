# wap to display the last digit of a no and ensure that num is divisible bt 3.

number=int(input("enter the no.: "))
N=number%10
print(f"{N} is the last digit of given number")
if number%3==0:
    print(f"{number} is divisible by 3")
else:
    print(f"{number} is not divisible by 3")