def convert_temp(celsuis):
    farenheit = (celsuis*5/9)+32
    mess_1 = " degrees celsuis are "
    mess_2 = " farenheit"
    return str(celsuis)+mess_1+str(farenheit)+mess_2

user_input = input("choose your temperature in celsuis degree: ")
farenheit_result = convert_temp (float(user_input))
print (farenheit_result)

if float(user_input) <= 21:
    input("it's to cold today")



