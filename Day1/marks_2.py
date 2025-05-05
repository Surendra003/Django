
#this is a global variable
marks=int(input("Enter a marks:"))
marks2=int(input("Enter a marks2:"))
print(marks+marks2)
def myfunction():
    #change values of global variable
    globals()['marks']=globals()['marks']+20 
    #OR method 2 downward 
    global marks2   #via global bata manipulate garna sakinxa
    marks2=marks2+40    
myfunction()
print("marks:",marks,"marks2:",marks2)    #print global value
print("Hello guys")