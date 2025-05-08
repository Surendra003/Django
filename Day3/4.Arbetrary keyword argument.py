def describe_person(**kwargs):
    """
    This function takes an arbetery number of keyword arguments and print details
    """
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
#calling the function with arbetery keyword arguments
describe_person(name="Surendra", age=22,City="Kathmandu",profession="Student")

#*args
def describe_me(*args):
    for name in args:
        print(f"Hello, {name}")
describe_me("Surendra","Sushant")