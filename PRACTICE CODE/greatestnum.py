a=int(input("Enter your first number: "))
b=int(input("Enter your secound number: "))
c=int(input("enter your third number: "))
if a>=b and a>=c :
    print("Greatest number is:", a)
elif b>=a and b>=c:
    print("Greatest number is:",b )
else:
    print("Greatest number is:",c)