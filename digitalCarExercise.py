class Car:
    def __init__(self, model, color, motorisation, speed):
        self.model = model
        self.color = color
        self.motorisation = motorisation
        self.speed = speed

    def run(self):
        print("This "+self.model+" runs at a speed of "+str(self.speed))
    
    def decoration(self):
        print("This "+self.model+" is a "+self.color+" one.")
    
    def motor(self):
        print("This "+self.model+" has a "+self.motorisation+" energy system.")

my_car = Car("Volvo", "blue", "diesel", 120)
your_car = Car("Kia", "red", "gazoil", 150)
her_car = Car("Peugeot", "grey", "++95", 140)

my_car.run()
my_car.decoration()
my_car.motor()

your_car.run()
your_car.decoration()
your_car.motor()

her_car.run()
her_car.decoration()
her_car.motor()


