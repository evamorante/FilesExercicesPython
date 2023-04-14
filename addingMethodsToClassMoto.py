class Moto:
    speed=0
    color=""
    weight=0
    model=""

suzuki = Moto()
print(Moto)

suzuki = Moto()
suzuki.speed=100
suzuki.color="red"
suzuki.weight=320
suzuki.model="monster"

honda = Moto()
honda.speed=120
honda.color="black"
honda.weight=290
honda.model="speeder"

print(suzuki.speed)
print(honda.speed)

class Moto:
    speed=0
    color=""
    weight=0
    model=""

    def run(self):
        print(self.model + " run at a " + str(self.speed) + " km/h speed.")
    def decoration(self):
        print("This "+self.model+ " model is a "+self.color+" one.")
    def energy(self, kind):
        print("This "+self.model+" model needs gazoline "+kind)



suzuki = Moto()
suzuki.speed=100
suzuki.color="red"
suzuki.weight=320
suzuki.model="monster"

honda = Moto()
honda.speed=120
honda.color="black"
honda.weight=290
honda.model="speeder"

suzuki.run()
suzuki.decoration()
honda.run()
honda.decoration()

suzuki.energy("SP95")  
honda.energy("SP98") 

