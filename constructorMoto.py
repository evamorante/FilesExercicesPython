class Moto:
    
    def __init__(self, model, color):
        self.model = model
        self.color = color
        
    
    def run(self):
        print("This "+self.color+" model "+self.model + " runs very fast")

suzuki = Moto("speeder", "red")
honda = Moto("hondeer", "black")
yamaha = Moto("yameer", "white")

suzuki.run()
honda.run()
yamaha.run()



#print(suzuki.speed)
#print(honda.speed)

