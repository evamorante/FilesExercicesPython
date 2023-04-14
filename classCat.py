class Cat:
    name=""
    species=""
    weight=0
    color=""
tom = Cat()
print(tom)

tom = Cat()
tom.name="Tom"
tom.species="Gouttiere"
tom.weight=0
tom.color="Orange"

athena = Cat()
athena.name="Athena"
athena.species="Angora"
athena.weight=3
athena.color="White"

print("Athena is a "+ athena.species + " cat.")
print("But Tom is a "+tom.species+" cat.")

