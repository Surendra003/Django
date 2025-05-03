marks=50
print(marks)
def myfunction():
    marks=70 #this is local variable "local prority is high than global variable"
    print(marks)
myfunction()
print(marks)    #print global value