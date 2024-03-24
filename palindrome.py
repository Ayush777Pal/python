#Palindrome
N=int(input("enter a number to check="))
temp=N
rev=0
while(N>0):
    digit=N%10
    rev=rev*10+digit
    N=N//10

if(rev==temp):
    print("Given number",temp, "palindrome")
else:
    print("Given number",temp, "is not palindrope number")