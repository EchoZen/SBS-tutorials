#Create 2 lists
#a: Using only methods from lists, remove the last element from my list1
#remove 1st element of mylist2, concatenate these 2 lists while adding string 'Hello' in between
list1=['Merry Christmas','Happy Holidays','Greetings','Farewell','Get Well Soon']
list2=['Love','Hope','Joy']
list1.pop()
list2.pop(0)
list1.append("Hello")
list1.extend(list2)
print(list1)
#b: Do it without using list methods
list1=['Merry Christmas','Happy Holidays','Greetings','Farewell','Get Well Soon']
list2=['Love','Hope','Joy']
print(list1[:len(list1)-1]+" Hello".split()+ list2[1:])