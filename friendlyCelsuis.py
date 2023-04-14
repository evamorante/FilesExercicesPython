#18.5 degrees Celsuis are 65.3 degrees Farenheit.

def temp_converter(Celsuis):
    Farenheit = (Celsuis*9/5+32)
    message_1 = " degrees Celsuis are "
    message_2 = "degrees Farenheit."
    return str(Celsuis)+message_1+message_2+str(Farenheit)
print (temp_converter(21.5))
print (temp_converter(-7))
print (temp_converter(11))
print (temp_converter(0))