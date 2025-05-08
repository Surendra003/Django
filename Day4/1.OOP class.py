class Car:

    def __init__(self,model,color):    #initializing
        self.color=color    #attribute
        self.model=model

    def honk(self): #method
        print("Beep Beep")
    def brake(self):
        print("brake")

#creating an object
my_car=Car("Toyota","red")
my_car.honk()
my_car.brake()