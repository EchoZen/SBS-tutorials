#Dots in hexagons
fignum= int(input("Enter figure number:"))

def numdots(fn):
    result=10
    for i in range(fn-1):
        result+=6
    return result

print(numdots(fignum))
