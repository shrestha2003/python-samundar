#otp generator
import random as r
val= r.random()
stri=str(val)
num=int(input("enter number of digit of otp you need: "))
print("your otp  is: ",stri[3:num+3])
