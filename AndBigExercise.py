# not running properly, try it again !!!
# and do the second way, the Nico's way to do this exercise too !!

weather = input("what is the weather today ?")
temperature = input("what is the temperature today ?")

if (weather == "raining" and temperature == "cold"):
    print("take an umbrella and a jacket")
elif (weather == "raining" and temperature == "warm"):
    print("take an umbrella and a t-shirt")
elif (weather == "sunny" and temperature == "cold"):
    print("take sunglasses and a jacket")
elif (weather == "sunny" and temperature == "warm"):
    print("take sunglasses and a t-shirt")
else:
    print("stay home!")

