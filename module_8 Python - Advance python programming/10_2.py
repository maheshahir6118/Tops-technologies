# Write a Python program to match a word in a string using re.match().
def check_number(n):
    match n:
        case 0:
            print("zero")
        case n if n>0:
            print("positive number")
        case _:
            print("negative number")
check_number(-2)