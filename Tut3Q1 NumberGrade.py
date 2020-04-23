User_numgrade= int(input("What is your numerical grade?"))
if User_numgrade>10 or User_numgrade<0:
    print("Impossible")
elif User_numgrade==10 or User_numgrade==9:
    print("You got an A")
elif User_numgrade==8:
    print("You got a B")
elif User_numgrade==7:
    print("You got a C")
elif User_numgrade==6:
    print("You got a D")
else:
    print("You got an F")
