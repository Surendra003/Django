"""def my_function(x):
    print("The number is: ",x)
def my_decorator(some_function,num):
    def wrapper(num):
        print("Inside wrapper to check odd/even")
        if num%2==0:
            ret="even"
        else:
            ret="odd"
        some_function(num)
        return ret
    print("Wrapper function is called")
    return wrapper
no=10
my_function=my_decorator(my_function,no)
print("It is ",my_function(no))"""

def my_decorator(some_function):
    def wrapper(num):
        print("inside wrapper to check odd or even.")
        if num%2==0:
            ret="Even"
        else:
            ret="Odd"
        some_function(num)
        return ret
    print("wrapper function is called")
    return wrapper
@my_decorator
def my_function(x):
    print("The number is:",x)
no=10
print("It is ",my_function(no))