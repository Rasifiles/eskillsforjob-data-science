a =10
b = 12
a < b
# question1
#first_number = int(input("Enter your first number"))
#second_number = int(input("Enter your second number"))

#if (first_number > second_number):
#    print(second_number, first_number)
#else:
 #   print(first_number, second_number)

# Question two
#     User_umber =  int(("input(Enter a number under 20")) 
# if(User_number>=20):
#     print(Too high) 
# else:
    #print(Thank you)

#question 3
# favourate_colour = input("Enter favourate colour")
# if((fourate_colour == red) or (fourate_colour == Red) or (fourate_colour == RED)):
#     print((I like red too) or (I like red too) or (I like red too))
# else:
#     print(I dont like colour)

# print("Enter [yes] or [no] to the following questions")
# user_input = input("Is it raining?")
# if(user_input == "yes"):
#    user_input_2 = input("Is it also windy?:")
#    if (user_input_2 =="yes"):
#        print("It is too windy for an umbrella")
#    else:
#         print("take an unbrella")
# else:
#     print("Enjoy your day")


#user_input = int(input("Enter age"))
#if

#Question1.
# print("Enter 1 or 2 or3")
# user_input = int(input('Enter a number of your choice'))
# if(user_input ==1):
#    print("thank you")
# elif(user_input ==2):
#     print("well done")
# elif(user_input == 3):
#     print("correct")
# else:
#     print("error massage")

# # #group_of_items = "moro"
# class_reg = ['Nat', 'Jul', 'Osca', 'Lyd']
# for each_item in class_reg:

# user_name = input("Enter your name: ")
# for each_name in range(1, 4):
# print("Your name is: Rasi")

# user_name = input("Enter your name")
# user_number = int(input("Enter a number of times"))
# if (user_number < 10):
#     for each_name in range(1, user_number + 1):
#         print(user_name)
# else:
#     for each_massage in range(1, 4):
#         print("Too high")

# Using a while loop
# again = "yes"
# again = input('Enter yes or no')
# while(again == "yes"):
#     print("Hello")
#     again = input("Do you want to continue")


# total = 0
# while(total <= 10):
#     print("Hellow woulrd")
#     total + 1
# print("goodbye")
#import random

# print("CLASS ATTENDANCE REGISTER")
# attendance = input("Have you registered or not ?")
# while(attendance == "no"):
#     username = input("Enter your name to register: ")
#     print("Confirm your name: ", username)
#     ## loop control
#     attendance = input("Have you registered or not ?")

# question. Ask a user to enter a number. Keep asking until they enter a value over 5 and then display the massage"The last number you entered was a number' and stop the program.
# User_input = 0
# while (User_input < 5):
#     # loop control
#       User_input = int(input("Enter a number: "))
#       print("The last number you entered was [", User_input, "]")
#       print(f"..............................................")
#       print(f"The last number you entered was [{User_input}]")

# 
## generate random numbers 
# import random
# rand_number = random. randint(0, 9)
# print(rand_number)

User_input = int(input("Enter a number b/n 10 and 20"))
while((User_input < 10) or (User_input > 20)):
    if User_input < 10:
        print('Too low')
        if User_input > 20:
            print("Too high")
            User_input = int(input('Enter the guess again'))
else:  
    print ("thankyou")