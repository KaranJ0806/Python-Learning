#Print a multiplication table using while loop 

# num = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(f"{num} x {i} = {num * i}")
#     i += 1



# print a menu driven program 
# # print ("Menu:")
# # 1. Hello
# #2. Message
# #3. Exit
# while True:
#     print("Menu:")
#     print("1. Hello")
#     print("2. Message")
#     print("3. Exit")
#     choice = input("Enter your choice (1-3): ")

#     if choice == '1':
#         print("Hello!")
#     elif choice == '2':
#         print("Hardwork is the key.")
#     elif choice == '3':
#         print("Exiting...")
#         break
#     else:
#        print("Invalid choice. Please try again.")


# Demonstrate break - find a number 
# write a python program that checks numbers from 1 to 20 
# if the number is 15, display " number found" and stop the loop using break.
# otherwise, display the number 
# i = 1
# while i <= 20:
#     if i == 15:
#         print("Number found")
#         break
#     else:
#         print(i)
#     i += 1



#Demonstrate continue - skip even numbers
#write a python program to print numbers from 1 to 20.
#use continue to skip even numbers and print only odd numbers.
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1



# Write a Python program to simulate a simple ATM. Assume the
# user's initial account balance is ₹10,000.

# # Display the following menu:

# # ========== ATM ==========

# # 1. Check Balance

# # 2. Withdraw Money

# # 3. Exit

# # ==========================

# # Enter your choice:

# # The program should repeatedly display the menu
# until the user chooses Exit.

# # If the user selects 1, display the current
# account balance.

# # If the user selects 2, ask the user to
# enter the amount they want to withdraw.

# # If the amount is 0 or negative, display
# "Invalid withdrawal amount."

# # If the amount is greater than the
# available balance, display "Insufficient balance."

# # If the amount is valid, process the
# withdrawal, deduct the amount from the balance, and display the remaining
# balance.

# # Continue asking for the withdrawal
# amount until a valid amount is entered.

# # If the user selects 3, display
# "Thank you for using the ATM." and terminate the program.

# # If the user enters any other choice,
# display "Invalid choice."

# # Use a while loop to repeatedly display the ATM
# menu and handle the user's choices

password= 1234 
balance = 10000
while True:
    print("========== ATM ==========")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Exit")
    print("==========================")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        print(f"Your current balance is: ₹{balance}")
        
    elif choice == '2':
            
            amount = float(input("Enter the amount to withdraw: ₹"))
            if amount <= 0:
                print("Invalid withdrawal amount.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print(f"Withdrawal successful. Remaining balance: ₹{balance}")
                break
                
    elif choice == '3':
        print("Thank you for using the ATM.")
        break
        
    else:
        print("Invalid choice.")



