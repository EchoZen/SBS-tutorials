
my_list= [2.70, 3.14 , 5.92, 9.26, 12.48, 30.40, 55.55 ]

#Normal search
def search(my_list, element):
    answer= False
    for i in my_list:
        print(i)
        if element== i:
            answer= True
            break
    return answer

print(search(my_list, 55.55))

#recursive binary search
#Question: if I use binary search, but use recursive, what Big O notation is it? myans(idk if correct)= 2log(n)
def binarysearch(my_list, element):
    length= len(my_list)//2
    answer= False
    if element== my_list[length]:
        answer= True
    else:
        if element> my_list[length]:
            list= my_list[length:]
            if binarysearch(list, element)== True:
                answer= True
        else:
            list= my_list[:length]
            binarysearch(list, element)
            if binarysearch(list, element)== True:
                answer= True
    return answer
print(binarysearch(my_list, 12.48))

#for loop binary search
def binarysearch(my_list, element):
    answer= False
    for i in range(len(my_list)):
        print(i)
        if element== my_list[len(my_list)//2]:
            answer= True
            break
        elif element> my_list[len(my_list)//2]:
            my_list = my_list[len(my_list)//2:]
        elif element< my_list[len(my_list)//2]:
            my_list = my_list[:len(my_list)//2]
    return answer

print(binarysearch(my_list, 55.55))
