num = input("Enter a number:")
num = int(num)

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

"""
if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
elif num == 4:
    print("Four")
elif num == 5:
    print("Five")
else:
    print("Not in list!")
"""

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case _:
        print("Not in list!")

