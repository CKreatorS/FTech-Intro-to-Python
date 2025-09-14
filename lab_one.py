"""
Caitlyn Morales
Created: 09/08/2025
Edited: 09/13/2025

Created a Python script that implements a simple units converter. 
Program first asks to pick from a menu of conversions. Then it asks for the input, 
performs the conversion, and displays the result.
"""

# Write out options
options = """

(1)Kelvin to Farenheit
(2)Farenheit to Kelvin
(3)Meters to Yards
(4)Yards to Meters
(5)Quit

"""

print("Welcome to Converter")

while True:
    print(options)
    try:
         selection = int(input("Please select from the following converting options: "))
    except ValueError:
        print("Invalid input, please enter a number between 1 and 5.")
        continue
        
    if (selection == 1):
        print("You selected Kelvin to Farenheit")
        kelvin = input(("Enter degrees in Kelvin: "))
        kelvin = (1.8*(float(kelvin)-273.15)+32)
        print(f"Your degrees in Farenheit is: {kelvin}")
        
    elif (selection == 2):
        print("You selected Farenheit to Kelvin")
        farenheit = input(("Enter degrees in Farenheit: "))
        farenheit = (((float(farenheit)-32)/1.8)+273.15)
        print(f"Your degrees in Kelvin is {farenheit}")

    elif (selection == 3):
        print("You selected Meters to Yards")
        meters = input(("Enter degrees in Meters: "))
        meters = (float(meters)*1.094)
        print(f"Your length in Yards is {meters}")

    elif (selection == 4):
        print("You selected Yards to Meters")
        yards = input(("Enter degrees in Yards: "))
        yards = (float(yards)/1.094)
        print(f"Your length in Meters is {yards}")

    elif (selection == 5):
        print("Thank you for using converter, goodbye.")
        break

    else:
        print("Please make a valid selection.")
        continue