names= ['Alex', 'Jacokb', 'Thomas', 'john']
sorted(names, key= str.lower)
print(names)

# Write your own comparison function and use it as a key function
# a) sort strings of the list alphabetically, but ignoring first letter
def nofirstletter(mystr):
    return mystr[1:]
print(sorted(names, key= nofirstletter)) #For key, function don't need bracket!

# # b) sort strings according to length
print(sorted(names, key= len))