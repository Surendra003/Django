def factorial():
    num=int(input("Enter a number tha you want to calculate factorial:"))
    factorial=1
    if num<0:
        print("You putted wrong number:")
    elif num==0:
        print("Factorial of your number is 1.")
    else:
        for i in range(1,num+1):
            factorial*=i
        print(f"The factorial of {num} is {factorial}.")
factorial()