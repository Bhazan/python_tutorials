# lambda arguments: expression

x = lambda a: a+10
print(x(5))

# lambda with multiple arguments
y = lambda a,b: a*b

print(y(4,5))

def myfunc(n):
    return lambda a: a*n

value = myfunc(5)

print(value(5))
