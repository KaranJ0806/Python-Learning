#def(to define a function) (function definition starts with def)
#def function_name(parameters): (parameters is optional)
#function_body ( function body is indented block )
#return value( optional)

# def greet(name):
#     print("Hello", name) # this is task performed by the function 

# greet('Karan') #this line means -> print ("Hello", 'Karan')
# greet('John')


#adding two numbers with the help of function
# def add_two_numbers(num1,num2):
#     print('Calculating addition of',num1,num2)
#     return (num1 + num2)


#print(add_two_numbers(2,4))

#addition_of_3_and_5 = add_two_numbers(3,5) # -> addition_of_3_and_5 = 8 
# print('Printing addition of 3 and 5:',add_two_numbers(3,5))



#write a program to calculate square of a number using function
# def square(num):
#     print('Calculating square of',num , )
#     return num * num

# print(square(5))




#write a program which will take name and age as input and prints the following message using function
# Hello John, you are 20 years old.
# user_name = input("Enter your name: ")
# user_age = input("Enter your age: ")
# def greet_user(user_name, user_age):
#     print("Hello", user_name ," You are", user_age, "Years old.")

# greet_user(user_name, user_age)




#write a program which will ask name and marks of the students then print whether passed or failed using function
#criteria for passing 40 out of 100
#output: congrats Karan' you are passed . or Hi Karan you are failed.
# user_name = input("Enter your name: ")
# user_marks = int(input("Enter your marks: "))

# def check_pass_fail(user_name, user_marks):
#     if user_marks >= 40:
#         print(f"Congrats {user_name}, you are passed.")
#     else:
#         print(f"Hi {user_name}, you are failed.")

# check_pass_fail(user_name, user_marks)




##write a program which will ask name and marks of the students then print whether passed or failed using function
#criteria for passing 40 out of 100
#the program will keep asking for student name and marks, also ask for exit 
#output: congrats Karan' you are passed . or Hi Karan you are failed.

def check_pass_fail(user_name, user_marks):
    if user_marks >= 40:
        print(f"Congrats {user_name}, you are passed.")
    else:
        print(f"Hi {user_name}, you are failed.")

while True:
    user_name = input("Enter your name (or type 'exit' to quit): ")
    if user_name == 'exit':
        print("Exiting program.")
        break

    user_marks = int(input("Enter your marks: "))
    check_pass_fail(user_name, user_marks)

    continue_choice = input("Do you want to continue? (y/n): ")
    if continue_choice == 'y':
        print("Exiting program.")
        break
