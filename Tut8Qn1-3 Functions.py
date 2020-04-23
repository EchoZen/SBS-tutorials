#1) Calculate rectangle area
def calcrectarea(width, height):
    return width*height
print("The area of the rectangle is", calcrectarea(6,10))

#2) Total amount of money in bank after n years
def totmoney(principle, interest, n):
    print("Principle: $"+str(principle))
    print("Interest rate:", interest)
    print("Years:", n)
    return principle*(1+interest)**n

print("Total money is $"+ str(totmoney(100,1,1)))

#3) Number of seconds in duration keyed by user
years= int(input("Enter number of years:"))
days= int(input("Enter days:"))
hours= int(input("Enter hours:"))
def seconds(years, days, hours):
    return ((years*365 + days)*24 + hours)*3600
print("There are", seconds(years, days, hours), "seconds in", years, "years,", days, "days and", hours, "hours.")