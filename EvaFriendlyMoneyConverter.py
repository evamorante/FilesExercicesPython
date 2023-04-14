def money_converter(chf):
    mess_1 = " Swiss Francs are " 
    mess_2 = " American Dollars."
    dollars = chf*1.05
    return str(chf)+mess_1+str(dollars)+mess_2

print(money_converter(34))
print(money_converter(23))
print(money_converter(66))