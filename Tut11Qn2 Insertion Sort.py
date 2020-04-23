inlist = [5, 234, 357, 110]
outlist= []

for i in inlist:
    for j in range(len(outlist)):
        if i< outlist[j]:
            outlist.insert(j,i) #insert i at index j
            break
    else:
        outlist += [i]

print(inlist)
print(outlist)