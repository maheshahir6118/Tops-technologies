# Write a Python program to handle exceptions in a simple calculator 
# (division by zero, invalid input)
num1=int(input("enter your first number : "))
num2=int(input("enter your second number : "))
op=input("enter operator (+,-,*,/):")
if op=='+':
    result=num1+num2
elif op=='-':
    result=num1-num2
elif op=='*':
    result=num1*num2
elif op=='/':
    result=num1/num2
else:
    print("Invalid choice ")
print(num1,op,num2," = ",result)