#Using the range function, create the following lists:
#a: [3,4,5,6]
list1=[]
for i in range(3,7):
    list1.append(i)
print(list1)
#b: [18,16,14,12]
list2=[]
for x in range(6,10):
    list2.append(x*2)
list2.reverse()
print(list2)
#c: [50, 45, 40, 35, 30, 5, 10, 15, 20, 25, 30]
list3=[]
for i in range(30,55,5):
    list3.append(i)
list3.reverse()
list4=[]
for i in range(5,35,5):
    list4.append(i)
list3.extend(list4)
print(list3)
