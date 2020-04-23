choice= int(input("Choose\n 1. Cylinder\n 2. Circle\n 3. Rectangle:"))
import math
if choice!=1 and choice!=2 and choice!=3:
    print("Invalid input")
else:
    if choice==1:
        radius= float(input("Enter radius:"))
        height= float(input("Enter height:"))
        cylinder= math.pi*radius*radius*2 + math.pi*radius*2*height
        print("Cylinder area is", cylinder)
    else:
        if choice==2:
            radius = float(input("Enter radius:"))
            circle= math.pi*radius*radius
            print("Area of circle is", circle)
        else:
            if choice==3:
                length= float(input("Enter length:"))
                width= float(input("Enter width:"))
                rect= length*width
                print("Rectangle area is", rect)
