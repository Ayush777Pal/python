n=int(input("Enter a numbr till you want fibonacci series"))
a=0
b=1
if(n==0):
    print("a")
elif(n==1):
    print("a")
else:
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(a)
        print(b)