def temp_converter(celsuis):
    farenheit = (celsuis*9/5+32)
    message_1 = " degrees Celsuis are "
    message_2 = " degrees Farenheit."
    return str(celsuis)+message_1+str(farenheit)+message_2
  # 2 lignes suivantes restantes du code repris pour la conversion de celsuis en farenheit du code de base
  #  print (temp_converter(21.5))
  #  print (temp_converter(-7))
user_input = input("Enter your choiced degree Celsuis to convert: ")
farenheit_result = temp_converter (float(user_input))
print(farenheit_result)

if float(user_input) > 42:
    print ("It's hot !")

# prochaine ligne - réafficher le résultat
#print(farenheit_result)



