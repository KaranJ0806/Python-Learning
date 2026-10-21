# # use of list 
# variable1 = 'Karan' #string
# variable2 = 19 #integer
# variable3 = 23.3 #float
# variable4 = False #bolen

# new_list = ['Karan','Jadhav', 19, 23.5, False]
# #syntax for list:
# #name_of_the_list = [elements seperated by comma(,)]
# print(type(new_list))#access list items using index
# print(new_list[4]) #to access from start to end
# print(new_list[-1])#to access from end to start
# print(new_list[1],new_list[3]) #to access multiple element

# print(type(new_list[4])) 
# print(type(new_list[-1]))
# print(type((new_list[1],new_list[3])))

# print(type(new_list[0:2])) # for accessing multiple items but in consecutive

# print(new_list)
# new_list.append(22)
# new_list.append("john")
# new_list.append(89.90)
# new_list.append(True)
# print("after adding new element: \n" ,new_list)


# test_list = [1,2,3]
# test_list_new = [11,22,33]

# test_list.append(test_list_new)
# print(test_list)
# print(test_list[0])


# test_list = [1,2,3]
# test_list_new = [77,88,99]

# test_list.extend(test_list_new)
# print(test_list_new)
# print(test_list_new[0])

# following would be the output
# append [[1, 2, 3, [11, 22, 33]]] # ; here list is extended 
# extend [1, 2, 3, [11, 22, 33]] # ; here list is extended 


# test_list = [1,2,3]
# test_list_new = [11,22,33]

# test_list.append (test_list_new)
# print("append" , test_list)
# print("extend", test_list_new)


fruits=["Apple","Bannana","Mango"]
print("after:",fruits)

# #add item at speific position
fruits.insert(2,'guava')
print("after:",fruits)

#sort the list 
fruits.sort(reverse=True)
print('reverse sorted list:',fruits)

list_test_number=[3,1,33,22,6,7,9,76]
print('orignal list',list_test_number)
print(id(list_test_number))

#copy a list-> copy()
duplicate_list=list_test_number
print('duplicate list',duplicate_list)
print('address of duplicated_list',id(duplicate_list))

list_test_number.append(12)
print('duplicate_list',duplicate_list)

copied_list= list_test_number.copy()
print('address of copied list',id(copied_list))
