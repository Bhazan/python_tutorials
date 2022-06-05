# if else statement

is_male = True
num1 = 81
num2 = 32
num3 = 45

if is_male:
    print("Yes")    # If block start with indentation that have only one statement!
print("out of if block!")

if is_male:
    print("Yes")
else:
    print("No")
print("Out of else block!")

if num1>num2:
    if num1>num3:
        print("num1 is greatest of all ",num1)
    else:
        print("num3 is greatest of all ",num3)
elif num2>num3:
    print("num2 is greatest of all",num2)
else:
    print("num3 is greatest of all second path",num3)
print("out of if else elif block!")
