integer=-1
while integer<0:
    integer = int(input("Enter a positive integer:"))

for i in range(integer+1):
    if i%2==0:
        pass
    elif i%2!=0:
        print(i)

#2nd solution
for i in range(1,integer+1,2):
    print(i)