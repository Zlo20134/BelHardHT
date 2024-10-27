some_list1 = [1, 2, 3, 4, 5]
print(some_list1)

some_list2 = [6, 7, 8, 9, 10]
print(some_list2)

some_list1.append(22)
print(some_list1)

some_list2.append(33)
print(some_list2)

some_list1.insert(0,15)
print(some_list1)

some_list2.insert(0,55)
print(some_list2)

some_list1.extend(some_list2)
print(some_list1)