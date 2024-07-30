def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        return "zeor cannot be divisible"
    else:
        return x/y
    
while True:
   print("SELECT THE OPTION")
   print("CHOOSE 1 FOR ADDITION")
   print("CHOOSE 2 FOR SUBTRACTION")
   print("CHOOSE 3 FOR MULTIPLICATION")
   print("CHOOSE 4 FOR DIVISION")
   ch=int(input("Enter your choise :"))
   if ch==1:
      num1=int(input("Enter the  first number :"))
      num2=int(input("Enter the  second number :"))
      print("Addtion of two number {} and {} is".format(num1, num2),add(num1,num2))
   elif ch==2:
      num1=int(input("Enter the  first number :"))
      num2=int(input("Enter the  second number :"))
      print("Subraction of two number {} and {} is".format(num1, num2),sub(num1,num2))
   elif ch==3:
     num1=int(input("Enter the  first number :"))
     num2=int(input("Enter the  second number :"))
     print("Multiplication of two number {} and {} is".format(num1, num2),mul(num1,num2))
   elif ch==4:
     num1=int(input("Enter the  first number :"))
     num2=int(input("Enter the  second number :"))
     print("Division of two number {} and {} is".format(num1, num2),div(num1,num2))
   elif ch==5:
       print("Thank you")
       break
   else:
     print("Invalid Input.Please choose from this option")
     
     
