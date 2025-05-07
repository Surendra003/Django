#User define function
def greet(name):
    return f"Hello, {name}!"
print(greet("Surendra"))

#Function with parameters
def add_numbers(a,b):
    return a+b
result=(add_numbers(2,4))
print(result)

#Lambda function
square=lambda x:x*x
print(square(4))

#2 Lambda function
n=lambda x:"Positive" if x>0 else "Negative" if x<0 else "Zero"
print(n(5))
print(n(-3))
print(n(0))

#3 Lambda function
#performing addition and multiplication in a single line
calc=lambda x,y:(x+y,x*y)
res=calc(3,4)
print(res)

#Resursive function
def factorial(m):
    if m==1 or m==0:
        return 1    #stopping point
    return m*factorial(m-1) #resursive call
print(factorial(4))