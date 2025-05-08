class BankAccount:
    def __init__(self,balance): #initializing
        self.__balance=balance

    def deposite(self,amount):
        self.__balance+=amount

    def get_balance(self):
        return self.__balance
    
#creating object
account=BankAccount(100)
account.deposite(50)
print(account.get_balance()) 

#2 ENCAPSULATION
class Student:
    def __init__(self,name,age):
        #private member
        self.name=name
        self.__age=age

    #getter method
    def get_age(self):
        return self.__age
    #setter method
    def set_age(self,age):
        self.__age=age

stud=Student('Surendra',22)
#retriving age using getter
print('Name:',stud.name, stud.get_age())

#CHANGING AGE USING SETTER
stud.set_age(23)

#Retriving age using getter
print('Name',stud.name, stud.get_age())
        