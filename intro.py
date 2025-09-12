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

"""
if statements, if-then statements, if-else statements, if-then-elif
"""

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
"""
Match-case scenarios
"""
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

"""
While Loops
"""
# x = 0
# while (x < 19):
#     print("Are we there yet?")
#     print("\n")
#     x+=1

# count = 5 
# guess = 0 
# answer = 100
# while(guess != answer):
#     question = input("Guess a number between 0 and 100: ")
#     guess = int(question)
#     count -= 1
#     if (count > 5):
#         print("Out of guesses.")
#         # break statements can be used to exit a loop
#         break
#     else:
#         print(f"You have {count} guesses left")
#         # continue statements skips to the next iteration
#         continue
# if (guess == answer):
#         print("Correct!")

"""
For Loops
"""

# for i in range(10):
#     print("something here 10x")

# # i defaults to starting at 0

# for i in range(2, 9):
#     print("something here from 2-8")

# for i in range(2,9,2):
#     print("2-8, that one only-evens answer")

"""
Lists in Loops
"""
# myList = [2, "Fred", 16.7]
# myList.append("Apples")
# # append adds to the end of the list

# print(len(myList))
# # produces the number length of the list 

# print(myList)
# myList.insert(2, "Barney")
# # inserts at a certain point within the list 

# print(myList)

# myList.pop(1)
# # removes value from the list and returns what was in that position

# myList.remove("Barney")
# # erases an element from the list

# myList.index("Fred")
# # searches through the list and finds the position of the element found

# myList1 = [5,4,7]
# myList1.sort()
# print(myList1)

# values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
# results = []

# for value in values:
#     if (value % 3 == 0):
#         results.append(value)
# print(results)

values = [1,2,3,4]
i = 1
j = 2
temp = values[i]
values[i] = values[j]
values[j] = temp
print(values)
