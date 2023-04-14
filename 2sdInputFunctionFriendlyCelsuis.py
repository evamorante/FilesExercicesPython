def convert_temp(celsuis):
    farenheit = (celsuis*9/5)+32
    mess_1 = " degrees celsuis are "
    mess_2 = " degrees farenheit"
    return str(celsuis)+mess_1+str(farenheit)+mess_2
   
user_input = input("choose a number: ")
farenheit_result = convert_temp (float(user_input))

print(farenheit_result)

