# Write Python programs to demonstrate method overloading and method overriding.
#overriding
print("example of overriding")
class bank:
    def interest_rate(self):
        return 5
class SBI(bank):
    def interest_rate(self):
        return 7
class HDFC(bank):
    def interest_rate(self):
        return 10
b1=bank()
print("normal interest rate : ",b1.interest_rate())
b1=SBI()
print("SBI interest rate : ",b1.interest_rate())
b1=HDFC()
print("HDFC interest rate : ",b1.interest_rate())

#overloading
print("\n\nexample of overloading")
class Calculator:
    def add(self, *numbers):
        return sum(numbers)

obj = Calculator()
print(obj.add(2, 3))
print(obj.add(1, 2, 3, 4))