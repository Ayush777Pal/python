#factorial
N=int(input("Enter a Number"))
fact=1
#Check whether given input is positive or negative
if N<0:
    print("factorial not possible")
elif N==0:
    print("Factorial of 0 is zero")
else:
    for i in range(1, N+1):      #we consider the dont consider the last value
     fact=fact*i

print("The factorial of", N ,"is", fact)
