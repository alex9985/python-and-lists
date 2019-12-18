#find smalest number in a list
#
my_list = []
num = int(input("Enter number of elements to put into the list "))
for i in range(1, num + 1):
    elem = int(input("Enter elements: "))
    my_list.append(elem)
print("Smallest element is ", min(my_list))
