a=int(input("Enter number A"))
b=int(input("Enter number B"))
ch=str(input("Choose input= +,-,/,*"))

if(ch=="+"):
    print(a,"+",b,"=",a+b)
elif(ch =='-'):
    print(a,"-",b"=",a-b)
elif(ch =='*'):
    print(a,"*",b,"=",a*b)
elif(ch=='/'):
    print(a,"/",b,'=',a//b)
else:
    print("Enter valid choice")


