a=str(input("enter the first string: "))
b=str(input("enter the second string: "))
m=len(a)
n=len(b)
c=(a+b)
k=len(c)
if(m==n):
	for i in range(0,k//2,1):
		print("{}{}".format(c[i],c[(i+(k+1)//2)]),end='')
		
else:
	print("they are not")
