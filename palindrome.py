#Wap to find palindrome for both number and strings

string=input("enter the string: ")
revstr=""
for i in string:
    revstr=i+revstr
if (string==revstr):
    print("palindrome")
else:
     print("Not palindrome")