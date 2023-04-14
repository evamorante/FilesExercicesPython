def temp_converter(Celsuis):
    Farenheit = (Celsuis*9/5+32)
    message_1 = " degrees Celsuis are "
    message_2 = "degrees Farenheit."
    return str(Celsuis)+message_1+message_2+str(Farenheit)
print (temp_converter(21.5))
print (temp_converter(-7))
print (temp_converter(11))
print (temp_converter(0))
input("Enter your choiced degree Celsuis to convert: ")
# now il faut "lier" la fonction du convertisseur et le input....comment ? mystère
