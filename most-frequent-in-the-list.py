def most_frequent(list1):
    my_dict = {}
    count, item = 0, ''
    for i in list1:
        my_dict[i] = my_dict.get(i, 0) + 1
        if my_dict[i] >= count:
            count, item = my_dict[i], i
    return(item, count)

list2 = input("enter content of the list: ")
print(most_frequent(list2))
