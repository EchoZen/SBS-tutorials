#4) population density
country= input("Enter country:")
population= int(input("Enter population count:"))
area= float(input("Enter area of country (km^2):"))
def pop_den(population, area):
    return round(population/area)
print(country, "has a population density of", pop_den(population, area), "people per km^2.")

#5)Function that outputs how many time character occurs in string
#and the indexes of the characters in the string in a list
my_str=input("Enter a string:")
char=input("Enter a character to check in string:")
def occurences(my_str, char):
    index=[]
    count=0
    countindex=-1
    for i in my_str:
        countindex+=1
        if i== char:
            count+=1
            index.append(countindex)
        else:
            pass
    return count, index

print(occurences(my_str, char))