def adding(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print("please select your option:")
print("1.Adding")
print("2.Subtract")
print("3.Multiply")
print("4.Division")

choice=input("enter your choice :")
n1=float(input("enter your first number :"))
n2=float(input("enter your second number :"))
if (choice=='1'):
    print(n1,"+",n2,"=",adding(n1,n2))
elif(choice=='2'):
    print(n1,"-",n2,"=",subtract(n1,n2))
elif(choice=='3'):
    print(n1,"x",n2,"=",multiply(n1,n2))
elif(choice=='4'):
    print(n1,"/",n2,"=",divide(n1,n2))
else:
    print("Invalid data")




