"""
Caitlyn Morales
Created: 09/08/2025
Edited: 09/08/2025

Created a Python script that implements a simple units converter. 
Program first asks to pick from a menu of conversions. Then it asks for the input, 
performs the conversion, and displays the result.
"""

options = """

(1)Kelvin to Farenheit
(2)Farenheit to Kelvin
(3)Meters to Yards
(4)Yards to Meters
(5)Quit

"""

print("Welcome to Converter")
print(options)
selection = input("Please select from the following converting options: ")

match selection:
    case '1':
        print("You selected Kelvin to Farenheit")
    case '2':
        print("You selected Farenheit to Kelvin")
    case '3':
        print("You selected Meters to Yards")
    case '4':
        print("You selected Yards to Meters")
    case '5':
        print("Goodbye")
    case '_':
        print("Please make a selection")