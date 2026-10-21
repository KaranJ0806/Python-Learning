# products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Processor", "RAM", "Speakers" ]

# user_input = input('enter product name: ')

# #for loop program with flag 
# products_found = False

# for temp_var_name in products:
#     if temp_var_name.lower() == user_input.lower():
#         products_found = True
        

# if products_found==True:
#     print(f"{user_input} is available in the list.")
# else:
#     print(f"{user_input} is not available in the list.")

#print all items from a list 
# for item in products:
#     print(item)  


# for temp_var_name in range(10): #syntax for range is range ( Last Value)
#     print(temp_var_name)

# for temp_var_name in range(2, 10): #syntax for range is range ( Start Value, Stop Value)
#     print(temp_var_name)

# for temp_var_name in range(2, 15, 3): #syntax for range is range ( Start, Stop , increment by)
#     print(temp_var_name)

# for temp_var_name in range(10, 0, -1): #syntax for range is range ( Start, Stop , decrement by)
#     print(temp_var_name)

# for temp_var_name in range(10, 0, -2): #syntax for range is range ( Start, Stop , decrement by)
#     print(temp_var_name) 

#write program to launch rocket countdown timer, end statement should be "rocket launched"
#expected output:
#10
#9 and so on
# Rocket Launched

# print("Rocket Launching in")

# for i in range(10, 0, -1):
#     print(i)

# print("Rocket Launched")


#write program to print squares of numbers from 5 to 15
#output should be ,
# Square of 5 = 25 
# Square of 6 = 36 and so on
# print("Squares of numbers from 5 to 15 are:")
# for i in range(5, 16):
#     print(f"Square of {i} = {i**2}")


#write program to print numbers divisible by 5 between 1 to 100
#output should be 5,10,15.....100
# print("Numbers divisible by 5 between 1 to 100 are:")
# print(", ".join(str(i) for i in range(5, 101, 5)))


#write a program to get 5 number from user and display their sum.
#please input numbers : 1 2 3 4 5
#sum of numbers is : 15 
#use for loop to read the input from user 

# user_input = 0
# sum = 0
# numbers_count = int(input ('Please enter how many numbers do you want to add:'))
# for i in range(numbers_count):
#     user_input = int(input(f"Please enter number{i+1} "))# please enter number 1, please enter number 2
#     #print('The entered number is:', user_input)
#     sum = sum + user_input

# print('Current sum Value is:','' {sum}'')# The sum of the 5 numbers entered is : (Print Answer)



#print the following pattern using for loop 
# 0 1 2     ;line 1 
# 0 1 2    
# 0 1 2   
# 0 1 2     ;line 4

# for i  in range(6):
#     print(f"Row {i + 1}:", end=" ")
#     for j in range(8):
#         print(j,end=" ")
#         #inner loop ends 
#     print()


#print the following pattern using for loop 
# Row 0: 0
# Row 1 : 0 1 
# Row 2 : 0 1 2 
# Row 3 : 0 1 2 3
# Row 4 : 0 1 2 3 4 
 
# for i in range( 5,0, -1):
#     print(f"Row {5 -i}:", end=" ")
#     for j in range(i):
#         print(j, end=" ")
#     print()


# for i in range( 5,0, -1):
#     print(f"Row :", end=" ")
#     for j in range(i - 1, -1, -1):
#         print(j, end=" ")
#     print() 

#using for loop 
######################
#                    #
#                    #
#                    #
######################


# for i in range(5):
# 	for j in range(21):
# 		if i == 0 or i == 4 or j == 0 or j == 20:
# 			print("#", end="")
# 		else:
# 			print(" ", end="")
# 	print()



row= int(input("length of rectangle"))
column= 