#Discussion 1
value=6
if value%2==0:
    print("first", value)
elif value%3==0:
    print("second",value)

#first 6

while value<=9:
    value+=1
    if value==8:
        continue
    else:
        pass
    print("third", value)
else:
    print("fourth",value)

print("fifth",value)

#third 7 third 9 third 10 fourth 10 fifth 10

#Discussion 2
str=""
count=0
#while str!="####":
    #str= input("Enter a string:")
    #for letter in str:
        #if letter=="a":
            #count+=1
            #break
print(count, "strings w letter a")

#Discussion 3
F1=1
F2=1
F3=0
print(F1)
print(F2)
while F3<1000:
    F3=F1+F2
    if F3>1000:
        break
    print(F3)
    F1,F2=F2,F3

#Discussion 4
n= int(input("Enter a number:"))
for i in range(1,n+1):
    print("*"*i)
for i in range(n-1,0,-1):
    print("*"*i)

width = int(input("Please enter pattern width: "))
for i in range (width * 2):
    count = i
    if i > width:
        count = width * 2 - count
    print("*"*count)