# print("Hello World!")
#     # prints Hello World!

# myVariable = 8*9
# print(myVariable)
#     # prints the value stored in myVariable
# print("myVariable")
#     # prints myVariable
# input("Enter into terminal: ")
#     # creates an input area in the terminal''

# myName = input("Type your name: ")
#     # assigns myName to the input
# print(myName)
#      # prints the name entered into input

# input_name = input("Hello, what is your name?\n").strip()
#     # input takes a str name after the written str on a new line \n
#     # strip removes unecessary whitespace from beginning and end of input
# print("Hello " + input_name)
#     # prints the inputted name after the written str

# if statements, if-then statements, if-else statements, if-then-elif

# grade = 100
# # if (grade > 60):
# #     print("You pass the class.")
# # else:
# #     print("You fail.")

# if(grade >= 90):
#     print("A")
# elif(grade >= 80):
#     print("B")
# elif(grade >= 70):
#     print("C")
# elif(grade >= 60):
#     print("D")
# else:
#     print("F")

# # Match-case scenarios

# foodOption = input("What would you like for lunch? ")
# match foodOption:
#     case 'sandwhich':
#         print("You selected sandwich.")
#     case 'pizza':
#         print("You selected pizza.")
#     case 'sushi':
#         print("You selected sushi.")
#     case _:
#         print("We dont have that.")

# While Loops

# x = 0
# while (x < 19):
#     print("Are we there yet?")
#     print("\n")
#     x+=1

count = 5 
guess = 0 
answer = 100
while(guess != answer):
    question = input("Guess a number between 0 and 100: ")
    guess = int(question)
    count -= 1
    if (count > 5):
        print("Out of guesses.")
        # break statements can be used to exit a loop
        break
    else:
        print(f"You have {count} guesses left")
        # continue statements skips to the next iteration
        continue
if (guess == answer):
        print("Correct!")