import random
n=random.randint(0,11)
v=int(input("enter your guessed number: "))
print('random number n :',n)
if(n==v):
	print("your guessed number is right")
else:
		print("the guessed number is wrong")

