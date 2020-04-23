distance= float(input("Enter travel distance:"))
m_cost=distance*0.22
car_cost=distance*0.26
plane_cost=distance*0.78
if distance<0:
    print("Error:Value is negative.")
elif distance<20:
    print("Walking is free!")
    print("The cost by motorcycle is", m_cost, "SGD.")
    print("The cost by car is", car_cost, "SGD.")
    print("Your travel is too short to travel by plane.")
elif distance>20 and distance<100:
    print("Your travel is too long to be done by walking.")
    print("The cost by motorcycle is", m_cost, "SGD.")
    print("The cost by car is", car_cost, "SGD.")
    print("Your travel is too short to travel by plane.")
elif distance>20 and distance<200:
    print("Your travel is too long to be done by walking.")
    print("The cost by motorcycle is", m_cost, "SGD.")
    print("The cost by car is", car_cost, "SGD.")
    print("The cost by plane is", plane_cost, "SGD.")
elif distance>200 and distance<800:
    print("Your travel is too long to be done by walking.")
    print("Your travel is too long to be done by motorcycle.")
    print("The cost by car is", car_cost, "SGD.")
    print("The cost by plane is", plane_cost, "SGD.")
else:
    print("Your travel is too long to be done by walking.")
    print("Your travel is too long to be done by motorcycle.")
    print("Your travel is too long to be done by car.")
    print("The cost by plane is", plane_cost, "SGD.")