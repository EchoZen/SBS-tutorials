
repeat = "Y"
total = 0
while repeat == "Y":
    pizza_type = int(input("Which pizza would you like to order? \n 1) Margherita ($15.50) " \
                           "\n 2) Marinara ($17.50) \n 3) Napoletana ($18)"))
    pizza_amt = int(input("How many?"))
    if pizza_type == 1:
        total1 = pizza_amt * 15.50
        total = total1 + total
    elif pizza_type == 2:
        total2 = pizza_amt * 17.50
        total = total2 + total
    else:
        total3 = pizza_amt * 18
        total = total3 + total
    repeat = input("Would you like to continue ordering? Y/N").upper()
print("Your bill is", total)

