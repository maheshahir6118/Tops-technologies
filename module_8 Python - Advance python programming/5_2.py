# Write a Python program to demonstrate handling multiple exceptions.
try:
    num1=int(input("enter your first  number : "))
    num2=int(input("enter your second number : "))
    result=num1/num2
    lst=[232,566,899]
    index=int(input("enter your index(0-2) : "))
    print("index element : ",lst[index])
    print(result)
except ZeroDivisionError :
    print("error, zero not divisible")
except ValueError:
    print("value error, enter wrong value")
except IndexError:
    print("index error, entered wrong index")
except Exception as e:
    print("unexpected error : ",e)
finally:
    print("program execute successfully : ")