
def sumNumber(n):
    if n>0:
        sum = n + sumNumber(n-1)
    else:
        sum = 0

    return sum

    
value = sumNumber(5)
print(value)