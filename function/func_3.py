# A function with multiple arguments
def my_function(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

my_function(arg3 = "Bhajan", arg1 = "Sachin", arg2 = "Mahendra") # calling function with key value, order doesn't matter

# default parameter value

def my_func(country = "India"):
    print(country)

my_func("USA")
my_func("England")
my_func()
my_func("Austrailia")