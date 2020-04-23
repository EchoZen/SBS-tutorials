print("This program will calculate the volume of a pyramid.\n You have to enter the length and width of the base, and height of the pyramid.\nEnter i or c after on the next prompt to indicated inches or centimeter.")
length= float(input("Enter length:"))
c_i = input("c or i:")
if c_i=="c":
    length= length/2.54
width= float(input("Enter width:"))
c_i = input("c or i:")
if c_i=="c":
    width= width/2.54
height= float(input("Enter height:"))
c_i = input("c or i:")
if c_i=="c":
    height= height/2.54
volume= 1/3*length*width*height
print("Volume of pyramid is", volume, "cubic inches")