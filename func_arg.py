#def add(num1=0, num2=0):   # fixed arguments
#    return num1 + num2

def add(num1, *num2):   # variable length argument
    
    sum = num1
    for n in num2:
        sum += n

    return  sum

result = add(2,3,4,5,10,100,99)
print(result)

def person(name, **key_arg):  # keyword arguments
    print("name:", name)
    for k,v in key_arg.items(): # access variable length args as divt (key:value)
        print(k,":", v)

person(age=30,name="ABC",loc="BLR",day="Mon")   # argument order is different from def - resolved by keyword


