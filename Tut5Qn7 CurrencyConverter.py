SGD= float(input("Enter SGD:"))
if SGD<0:
    print("Error. Value is negative")
else:
    exchange= input("Do you want to convert this amount in Euros (E), US dollars (U) or Japanese (J)?").upper()
    if exchange=="E":
        print(SGD*0.66,"Euros")
    elif exchange=="U":
        print(SGD*0.72,"USD")
    elif exchange=="J":
        print(SGD*78.96,"yen")
    else:
        print("No foreign exchange currency available for this country")