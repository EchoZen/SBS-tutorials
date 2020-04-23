#a
L=[34, 2, 45, 10, -2, 6]
L.sort()
print(L)
#b
L=[34, 2, 45, 10, -2, 6]
L.append(13)
print(L)
#c
L=[34, 2, 45, 10, -2, 6]
L.reverse()
print(L)
#d: find index of element 34
L=[34, 2, 45, 10, -2, 6]
print(L.index(34))
#e: remove element 10
L=[34, 2, 45, 10, -2, 6]
L.remove(10)
print(L)
#f: display sublist of 2nd and 3rd element
L=[34, 2, 45, 10, -2, 6]
print(L[1:3])
#g: display sublist from 3rd to last element
L=[34, 2, 45, 10, -2, 6]
print(L[2:])