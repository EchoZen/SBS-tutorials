pH= float(input("Enter pH:"))
if pH<0 or pH>14:
    print("Error")
elif pH==7:
    print("Neutral")
elif pH<7:
    print("Acidic")
else:
    print("Basic")